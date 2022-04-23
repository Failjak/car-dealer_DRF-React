import django_filters
from django.db.models import Q

from apps.models import Dealer


class DealerFilter(django_filters.rest_framework.FilterSet):
    cars = django_filters.CharFilter(method='cars_filter', help_text='Also get cars by brand/model')

    def cars_filter(self, queryset, name, value):
        return queryset.filter(
            Q(car_prices__car__brand=value) |
            Q(car_prices__car__model=value)
        )

    class Meta:
        model = Dealer
        fields = {
            'name': ('exact', 'icontains'),
            'address__country': ('exact', 'icontains'),
            'address__city': ('exact', 'icontains'),
            'address__area': ('exact', 'icontains'),
            'address__street': ('exact', 'icontains'),
            'address__building': ('exact', 'icontains'),
        }
