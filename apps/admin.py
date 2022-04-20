from django.contrib import admin

from apps.models import Profile, Dealer, DealerAddress, Car, CarPrice, Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass


@admin.register(Car, CarPrice)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Dealer, DealerAddress)
class DealerAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

