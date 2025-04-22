import pydantic
import typing

from .shipping_rate_currency_option import ShippingRateCurrencyOption


class ShippingRateFixedAmountCurrencyOptions(pydantic.BaseModel):
    """
    Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, ShippingRateCurrencyOption]
