import pydantic
import typing
import typing_extensions

from .shipping_rate_update_body_fixed_amount_currency_options import (
    ShippingRateUpdateBodyFixedAmountCurrencyOptions,
    _SerializerShippingRateUpdateBodyFixedAmountCurrencyOptions,
)


class ShippingRateUpdateBodyFixedAmount(typing_extensions.TypedDict):
    """
    Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
    """

    currency_options: typing_extensions.NotRequired[
        ShippingRateUpdateBodyFixedAmountCurrencyOptions
    ]


class _SerializerShippingRateUpdateBodyFixedAmount(pydantic.BaseModel):
    """
    Serializer for ShippingRateUpdateBodyFixedAmount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency_options: typing.Optional[
        _SerializerShippingRateUpdateBodyFixedAmountCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
