from __future__ import annotations

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

    def update_status(self, status: OfferStatus):
        self.status = status.value
        self.save()

    @classmethod
    def get_users_offers(cls, user):
        """
        Get offers belonging to this profile/user
        """
        if not hasattr(user, 'user'):
            user = user.profile
        return cls.objects.filter(profile=user)

    @classmethod
    def get_users_cars(cls, user):
        """
        Get cars belonging to this profile/user
        """

        if not hasattr(user, 'user'):
            user = user.profile

        return [{"car": offer.car.car, "price": offer.car.price}
                for offer in cls.objects.filter(profile=user, status=OfferStatus.SUCCESS.value)]

    def __str__(self):
        return f"Offer to {self.profile.user.username}, ({self.id})"
