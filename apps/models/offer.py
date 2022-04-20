from django.db import models

from apps.mixins.timestamp import TimeStampModelMixin


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
        'apps.CarPrice',
        related_name='offer',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Offer to {self.profile.user.username}, ({self.id})"
