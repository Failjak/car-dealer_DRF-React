from django.contrib.auth.models import User
from django.db import models

from apps.common.types import CurrencyType


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(
        choices=CurrencyType.choices(),
        default=CurrencyType.USD.value,
        max_length=6
    )

    def __str__(self):
        return self.user.username
