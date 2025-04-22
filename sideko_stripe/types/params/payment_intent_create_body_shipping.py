import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_shipping_address import (
    PaymentIntentCreateBodyShippingAddress,
    _SerializerPaymentIntentCreateBodyShippingAddress,
)


class PaymentIntentCreateBodyShipping(typing_extensions.TypedDict):
    """
    Shipping information for this PaymentIntent.
    """

    address: typing_extensions.Required[PaymentIntentCreateBodyShippingAddress]

    carrier: typing_extensions.NotRequired[str]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[str]

    tracking_number: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentCreateBodyShipping(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyShipping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerPaymentIntentCreateBodyShippingAddress = pydantic.Field(
        alias="address",
    )
    carrier: typing.Optional[str] = pydantic.Field(alias="carrier", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    tracking_number: typing.Optional[str] = pydantic.Field(
        alias="tracking_number", default=None
    )
