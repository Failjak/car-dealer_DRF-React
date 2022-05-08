from rest_framework import status

from apps.models import Offer
from apps.common.types import OfferStatus
from apps.api.errors import BaseError


def handle_user_offer(offer: Offer):
    profile = offer.profile
    car_price = offer.car

    try:
        if car_price.count < 1:
            raise BaseError(details={
                'message': "No car available at the Dealership",
                'error': status.HTTP_400_BAD_REQUEST
            })

        profile.buy_car(car_price)
        car_price.count -= 1
        car_price.save()
        offer.update_status(OfferStatus.SUCCESS)

    except BaseError as e:
        offer.update_status(OfferStatus.FAILED)
        raise BaseError(details=e.details)

