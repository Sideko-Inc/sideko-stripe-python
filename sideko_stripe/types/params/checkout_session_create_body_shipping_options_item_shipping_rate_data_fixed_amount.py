import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_shipping_options_item_shipping_rate_data_fixed_amount_currency_options import (
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptions,
    _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptions,
)


class CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmount(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmount
    """

    amount: typing_extensions.Required[int]

    currency: typing_extensions.Required[str]

    currency_options: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptions
    ]


class _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmount(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmount handling case conversions
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
        _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
