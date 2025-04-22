import pydantic
import typing
import typing_extensions

from .checkout_session_update_body_shipping_options_arr0_item_shipping_rate_data_fixed_amount_currency_options_additional_props import (
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
    _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
)


class CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptions(
    typing_extensions.TypedDict, total=False
):
    """
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptions
    """


class _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptions(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str,
        _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
    ]
