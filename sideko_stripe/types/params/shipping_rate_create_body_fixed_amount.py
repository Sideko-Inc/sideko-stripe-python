import pydantic
import typing
import typing_extensions

from .shipping_rate_create_body_fixed_amount_currency_options import (
    ShippingRateCreateBodyFixedAmountCurrencyOptions,
    _SerializerShippingRateCreateBodyFixedAmountCurrencyOptions,
)


class ShippingRateCreateBodyFixedAmount(typing_extensions.TypedDict):
    """
    Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
    """

    amount: typing_extensions.Required[int]

    currency: typing_extensions.Required[str]

    currency_options: typing_extensions.NotRequired[
        ShippingRateCreateBodyFixedAmountCurrencyOptions
    ]


class _SerializerShippingRateCreateBodyFixedAmount(pydantic.BaseModel):
    """
    Serializer for ShippingRateCreateBodyFixedAmount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    currency_options: typing.Optional[
        _SerializerShippingRateCreateBodyFixedAmountCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
