import pydantic
import typing
import typing_extensions

from .price_create_body_currency_options_additional_props import (
    PriceCreateBodyCurrencyOptionsAdditionalProps,
    _SerializerPriceCreateBodyCurrencyOptionsAdditionalProps,
)


class PriceCreateBodyCurrencyOptions(typing_extensions.TypedDict, total=False):
    """
    Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    """


class _SerializerPriceCreateBodyCurrencyOptions(pydantic.BaseModel):
    """
    Serializer for PriceCreateBodyCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str, _SerializerPriceCreateBodyCurrencyOptionsAdditionalProps
    ]
