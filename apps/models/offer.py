from django.db import models

from apps.mixins.timestamp import TimeStampModelMixin
from ..common.types import OfferStatus


class Offer(TimeStampModelMixin):
    status = models.CharField(
        choices=OfferStatus.choices(),
        default=OfferStatus.PROCESS.value,
        max_length=7,
    )

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
        'apps.CarPrice',
        related_name='offer',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Offer to {self.profile.user.username}, ({self.id})"
