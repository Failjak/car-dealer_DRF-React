from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from apps.models import Car, DealerAddress


@dataclass()
class DealerStatistic:
    id: int
    name: str
    address: DealerAddress
    count_cars: int
    avg_car_price: Decimal
    max_car_price: Decimal
    most_popular_car: Car | None
