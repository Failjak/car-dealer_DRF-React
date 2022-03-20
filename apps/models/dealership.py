from django.db import models


class Dealer(models.Model):
    """
    Dealer information
    """
    name = models.CharField(max_length=255)
    car_prices = models.ManyToManyField('CarPrice')


class DealerAddress(models.Model):
    """
    Dealer address information model class
    """
    dealer = models.ForeignKey(
        'Dealer',
        on_delete=models.CASCADE,
        related_name='dealer_address'
    )

    flat_no = models.SmallIntegerField(null=True)
    building = models.CharField(max_length=300, help_text='Building number or name')
    street = models.CharField(max_length=300)
    area = models.CharField(max_length=300, help_text='Area, state, province')
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=2, help_text='ISO2 country code')
    postal_code = models.CharField(max_length=16, blank=True)
