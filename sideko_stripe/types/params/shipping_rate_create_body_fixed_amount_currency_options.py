import pydantic
import typing
import typing_extensions

from .shipping_rate_create_body_fixed_amount_currency_options_additional_props import (
    ShippingRateCreateBodyFixedAmountCurrencyOptionsAdditionalProps,
    _SerializerShippingRateCreateBodyFixedAmountCurrencyOptionsAdditionalProps,
)


class ShippingRateCreateBodyFixedAmountCurrencyOptions(
    typing_extensions.TypedDict, total=False
):
    """
    ShippingRateCreateBodyFixedAmountCurrencyOptions
    """


class _SerializerShippingRateCreateBodyFixedAmountCurrencyOptions(pydantic.BaseModel):
    """
    Serializer for ShippingRateCreateBodyFixedAmountCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str, _SerializerShippingRateCreateBodyFixedAmountCurrencyOptionsAdditionalProps
    ]
