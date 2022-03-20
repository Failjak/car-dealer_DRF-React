from django.db import models


class TimeStampModelMixin(models.Model):
    """
    Time stamp model mixin
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
