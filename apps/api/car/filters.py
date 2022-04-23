import django_filters

from apps.models import CarPrice


class CarPriceFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = CarPrice
        fields = {
            'price': ('exact', 'gte', 'lte'),
            'currency': ('exact', ),
            'count': ('exact', 'gte', 'lte'),
            'car__release_year': ('exact', 'gte', 'lte'),
            'car__brand': ('exact', 'icontains'),
            'car__model': ('exact', 'icontains'),
            'car__drive': ('exact', ),
            'car__transmission': ('exact', ),
        }
