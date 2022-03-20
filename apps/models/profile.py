from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(
        'Currency',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

