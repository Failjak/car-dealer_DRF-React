from django.db import models

from apps.mixins.timestamp import TimeStampModelMixin
from apps.common.types import CurrencyType


class Offer(TimeStampModelMixin):
    profile = models.ForeignKey(
        'apps.Profile',
        related_name='offer',
        on_delete=models.PROTECT
    )

    dealer = models.ForeignKey(
        'apps.Dealer',
        related_name='offer',
        on_delete=models.PROTECT
    )

    car = models.ForeignKey(
        'apps.Car',
        related_name='offer',
        on_delete=models.PROTECT
    )

    currency = models.CharField(
        choices=CurrencyType.choices(),
        default=CurrencyType.USD,
        max_length=6
    )
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Offer to {self.profile.user.username}, ({self.id})"
