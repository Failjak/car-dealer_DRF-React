from .types import CurrencyRate, CurrencyType
from decimal import Decimal


def transfer_between_currency(amount: Decimal, currency: CurrencyType, target_currency: CurrencyType) -> Decimal:
    """
    Transfer amount between two currencies
    """
    if currency == target_currency:
        return amount

    currency_rate = CurrencyRate[currency.name].value
    target_currency_rate = CurrencyRate[currency.name].value

    return Decimal((amount / currency_rate) * target_currency_rate)
