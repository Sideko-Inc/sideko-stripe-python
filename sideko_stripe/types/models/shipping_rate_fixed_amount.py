import pydantic
import typing

from .shipping_rate_fixed_amount_currency_options import (
    ShippingRateFixedAmountCurrencyOptions,
)


class ShippingRateFixedAmount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    A non-negative integer in cents representing how much to charge.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    currency_options: typing.Optional[ShippingRateFixedAmountCurrencyOptions] = (
        pydantic.Field(alias="currency_options", default=None)
    )
    """
    Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """
