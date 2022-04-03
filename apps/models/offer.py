from django.db import models

from enumchoicefield import EnumChoiceField
from apps.mixins.timestamp import TimeStampModelMixin
from apps.common.types import CurrencyType


class Offer(TimeStampModelMixin):
    user = models.ForeignKey(
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

    currency = EnumChoiceField(CurrencyType, default=CurrencyType.USD)
    price = models.DecimalField(max_digits=7, decimal_places=2)
