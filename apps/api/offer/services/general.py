from apps.models import Offer, CarPrice, Profile


def handle_user_offer(offer: Offer):
    profile = offer.profile
    car_price = offer.car
    dealer = offer.dealer

    car_cost = car_price.price
    if profile.currency != car_price.currency:
        # TODO lead to a similar currency
        pass

    if profile.balance < car_cost:
        raise  # TODO create errors

    # profile.balance -= car_cost
    # TODO logic