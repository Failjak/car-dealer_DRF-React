import operator
from decimal import Decimal

from PyPDF2 import PdfFileReader
from django.db.models import Avg, Max
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4


from ..models import Dealer
from .dataclasses import DealerStatistic


def generate_report_name(dealer=None) -> str:
    # TODO generate report name using datetime
    return 'test_name'


def make_dealers_report():
    title = generate_report_name()
    canvas = Canvas(title, pagesize=A4)
    canvas.setTitle(title)

    canvas.save()


def make_dealer_report(dealer: Dealer):
    pass


def get_dealers_statistic(dealers: list[Dealer]):
    result = []
    for dealer in dealers:
        stat = get_dealer_statistic(dealer)
        result.append(stat)

    return result


def get_dealer_statistic(dealer: Dealer):
    offers = dealer.offer.all()
    cars = dealer.car_prices.all()

    avg_price = cars.aggregate(Avg('price')).get('price__avg')
    max_price = cars.aggregate(Max('price')).get('price__max')

    car_count = {}
    for offer in offers:
        car = offer.car.car
        if car in car_count:
            car_count[car] += 1
        else:
            car_count[car] = 1
    popular_car = max(car_count.items(), key=operator.itemgetter(1), default=[None])[0]

    stat = DealerStatistic(
        id=dealer.id,
        name=dealer.name,
        address=dealer.address,
        count_cars=len(cars),
        avg_car_price=avg_price,
        max_car_price=max_price,
        most_popular_car=popular_car
    )

    return stat
