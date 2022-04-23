from django.db import models


class DealerAddress(models.Model):
    """
    Dealer address information model class
    """
    building = models.CharField(max_length=300, help_text='Building number or name')
    street = models.CharField(max_length=300)
    area = models.CharField(max_length=300, help_text='Area, state, province')
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=2, help_text='ISO2 country code')

    def __str__(self):
        return "%s, %s" % (self.country, self.city)


class Dealer(models.Model):
    """
    Dealer information
    """
    name = models.CharField(max_length=255)
    car_prices = models.ManyToManyField('CarPrice')
    address = models.OneToOneField(
        DealerAddress,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

