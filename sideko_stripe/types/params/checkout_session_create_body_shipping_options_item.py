import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_shipping_options_item_shipping_rate_data import (
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateData,
    _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateData,
)


class CheckoutSessionCreateBodyShippingOptionsItem(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyShippingOptionsItem
    """

    shipping_rate: typing_extensions.NotRequired[str]

    shipping_rate_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyShippingOptionsItemShippingRateData
    ]


class _SerializerCheckoutSessionCreateBodyShippingOptionsItem(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyShippingOptionsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    shipping_rate: typing.Optional[str] = pydantic.Field(
        alias="shipping_rate", default=None
    )
    shipping_rate_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateData
    ] = pydantic.Field(alias="shipping_rate_data", default=None)
