from django.db import models


class Dealer(models.Model):
    """
    Diller information
    """
    name = models.CharField(max_length=255)
    car_prices = models.ManyToManyField('CarPrice')

    def __str__(self):
        return self.name


class DealerAddress(models.Model):
    """
    Diller address information model class
    """
    dealer = models.ForeignKey(
        'Dealer',
        on_delete=models.CASCADE,
        related_name='dealer_address'
    )

    building = models.CharField(max_length=300, help_text='Building number or name')
    street = models.CharField(max_length=300)
    area = models.CharField(max_length=300, help_text='Area, state, province')
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=2, help_text='ISO2 country code')

    def __str__(self):
        return "%s - %s, %s" % (self.dealer.name, self.country, self.city)
