from django.contrib import admin

from apps.models import Profile, Dealer, DealerAddress, Car, CarPrice, Currency


@admin.register(Car, CarPrice)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Dealer, DealerAddress)
class DealerAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
