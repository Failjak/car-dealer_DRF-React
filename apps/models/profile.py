from django.contrib.auth.models import User
from django.db import models
from rest_framework import status

from apps.common.helpers import transfer_between_currency
from apps.common.types import CurrencyType
from apps.models import CarPrice
from apps.api.errors import BaseError


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    balance = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.CharField(
        choices=CurrencyType.choices(),
        default=CurrencyType.USD.value,
        max_length=6
    )

    def get_currency(self):
        return CurrencyType(self.currency)

    def buy_car(self, car: CarPrice):
        car_cost = transfer_between_currency(
            car.price,
            car.get_currency(),
            self.get_currency()
        )

        if self.balance < car_cost:
            raise BaseError(details={
                'message': 'Not enough money',
                'status': status.HTTP_400_BAD_REQUEST
            })

        self.balance -= car_cost
        self.save()

    def __str__(self):
        return self.user.username
