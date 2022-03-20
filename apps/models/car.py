import datetime
from django.utils.translation import gettext as _
from django.db import models


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


class Car(models.Model):
    """
    Car information
    """
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_year = models.IntegerField(_('year'), choices=year_choices(), default=current_year())

    DTIVES = (
        ('Front-wheel', 'F'),
        ('Rear-wheel', 'B'),
        ('All-wheel', 'Full')
    )

    drive = models.CharField(
        max_length=255,
        choices=DTIVES,
        help_text='\n'.join(map(lambda x: ' - '.join(str(y) for y in x), DTIVES))
    )

    TRANSMISSIONS = (
        ('Atomatic', 'A'),
        ('Manual', 'M')
    )

    transmission = models.CharField(
        max_length=255,
        choices=TRANSMISSIONS,
        help_text='\n'.join(map(lambda x: ' - '.join(str(y) for y in x), TRANSMISSIONS))
    )

    def __str__(self):
        return '%s %s, %s' % (self.brand, self.model, self.release_year)


class CarPrice(models.Model):
    """
    Price of car
    """
    car = models.ForeignKey(
        'Car',
        related_name='price',
        on_delete=models.CASCADE
    )

    currency = models.ForeignKey(
        'Currency',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    price = models.DecimalField(max_digits=7, decimal_places=2)
    count = models.PositiveSmallIntegerField()

    def __str__(self):
        return '%s %s - %s$ %spieces' % (self.car.brand, self.car.model, self.price, self.count)
