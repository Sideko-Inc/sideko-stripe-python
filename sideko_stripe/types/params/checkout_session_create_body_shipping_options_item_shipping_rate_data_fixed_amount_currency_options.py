import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_shipping_options_item_shipping_rate_data_fixed_amount_currency_options_additional_props import (
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
    _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
)


class CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptions(
    typing_extensions.TypedDict, total=False
):
    """
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptions
    """


class _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptions(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str,
        _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
    ]
