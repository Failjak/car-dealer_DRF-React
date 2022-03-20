from django.db import models

from apps.mixins.timestamp import TimeStampModelMixin


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

    # TODO money field
    # price =
