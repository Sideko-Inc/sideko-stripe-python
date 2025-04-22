import pydantic
import typing
import typing_extensions

from .checkout_session_update_body_shipping_options_arr0_item_shipping_rate_data import (
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateData,
    _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateData,
)


class CheckoutSessionUpdateBodyShippingOptionsArr0Item(typing_extensions.TypedDict):
    """
    CheckoutSessionUpdateBodyShippingOptionsArr0Item
    """

    shipping_rate: typing_extensions.NotRequired[str]

    shipping_rate_data: typing_extensions.NotRequired[
        CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateData
    ]


class _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0Item(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionUpdateBodyShippingOptionsArr0Item handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    shipping_rate: typing.Optional[str] = pydantic.Field(
        alias="shipping_rate", default=None
    )
    shipping_rate_data: typing.Optional[
        _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateData
    ] = pydantic.Field(alias="shipping_rate_data", default=None)
