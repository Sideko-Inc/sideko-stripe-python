import pydantic
import typing
import typing_extensions

from .price_update_body_currency_options_obj0_additional_props import (
    PriceUpdateBodyCurrencyOptionsObj0AdditionalProps,
    _SerializerPriceUpdateBodyCurrencyOptionsObj0AdditionalProps,
)


class PriceUpdateBodyCurrencyOptionsObj0(typing_extensions.TypedDict, total=False):
    """
    PriceUpdateBodyCurrencyOptionsObj0
    """


class _SerializerPriceUpdateBodyCurrencyOptionsObj0(pydantic.BaseModel):
    """
    Serializer for PriceUpdateBodyCurrencyOptionsObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str, _SerializerPriceUpdateBodyCurrencyOptionsObj0AdditionalProps
    ]
