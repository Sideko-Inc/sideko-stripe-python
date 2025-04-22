import pydantic
import typing
import typing_extensions

from .shipping_rate_update_body_fixed_amount_currency_options_additional_props import (
    ShippingRateUpdateBodyFixedAmountCurrencyOptionsAdditionalProps,
    _SerializerShippingRateUpdateBodyFixedAmountCurrencyOptionsAdditionalProps,
)


class ShippingRateUpdateBodyFixedAmountCurrencyOptions(
    typing_extensions.TypedDict, total=False
):
    """
    ShippingRateUpdateBodyFixedAmountCurrencyOptions
    """


class _SerializerShippingRateUpdateBodyFixedAmountCurrencyOptions(pydantic.BaseModel):
    """
    Serializer for ShippingRateUpdateBodyFixedAmountCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str, _SerializerShippingRateUpdateBodyFixedAmountCurrencyOptionsAdditionalProps
    ]
