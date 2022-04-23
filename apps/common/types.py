from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class CurrencyType(BaseEnum):
    USD = "USD"
    BYN = "BYN"
    RUB = "RUB"


class CurrencyRate(BaseEnum):
    USD = 1
    BYN = 2.9
    RUN = 100


class OfferStatus(BaseEnum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PROCESS = "PROCESS"
