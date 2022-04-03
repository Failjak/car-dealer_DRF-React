from django.contrib.auth.models import User
from django.db import models
from enumchoicefield import EnumChoiceField

from apps.common.types import CurrencyType


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = EnumChoiceField(CurrencyType, default=CurrencyType.USD)

    def __str__(self):
        return self.user.username
