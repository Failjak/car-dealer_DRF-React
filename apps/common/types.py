from enum import Enum


class CurrencyType(Enum):
    USD = "USD"
    BYN = "BYN"
    RUB = "RUB"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class CurrencyRate(Enum):
    USD = 1
    BYN = 2.9
    RUN = 100
