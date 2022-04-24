from apps.models import Offer, CarPrice, Profile
from apps.common.helpers import transfer_between_currency
from apps.common.types import OfferStatus
from apps.api.offer.errors import OfferError


def handle_user_offer(offer: Offer):
    profile = offer.profile
    car_price = offer.car

    if car_price.count < 1:
        raise OfferError(message="No car available at the Dealership")

    car_cost = transfer_between_currency(
        car_price.price,
        car_price.get_currency(),
        profile.get_currency()
    )

    if profile.balance < car_cost:
        raise OfferError(message="Not enough money")

    profile.balance -= car_cost
    # TODO adding car to user
    # profile.cars
    car_price.count -= 1

    profile.save()
    car_price.save()

    offer.status = OfferStatus.SUCCESS.value
