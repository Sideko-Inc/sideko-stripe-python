import pydantic
import typing
import typing_extensions

from .checkout_session_update_body_shipping_options_arr0_item_shipping_rate_data_fixed_amount_currency_options import (
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptions,
    _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptions,
)


class CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmount(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmount
    """

    amount: typing_extensions.Required[int]

    currency: typing_extensions.Required[str]

    currency_options: typing_extensions.NotRequired[
        CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptions
    ]


class _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmount(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmount handling case conversions
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
        _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
