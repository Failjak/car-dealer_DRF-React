from django.db import models


class Currency(models.Model):
    """
    Representation of a certain Currency (USD, EUR, etc.)
    """
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code
