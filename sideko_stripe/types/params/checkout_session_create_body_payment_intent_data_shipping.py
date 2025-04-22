import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_intent_data_shipping_address import (
    CheckoutSessionCreateBodyPaymentIntentDataShippingAddress,
    _SerializerCheckoutSessionCreateBodyPaymentIntentDataShippingAddress,
)


class CheckoutSessionCreateBodyPaymentIntentDataShipping(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyPaymentIntentDataShipping
    """

    address: typing_extensions.Required[
        CheckoutSessionCreateBodyPaymentIntentDataShippingAddress
    ]

    carrier: typing_extensions.NotRequired[str]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[str]

    tracking_number: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyPaymentIntentDataShipping(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPaymentIntentDataShipping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerCheckoutSessionCreateBodyPaymentIntentDataShippingAddress = (
        pydantic.Field(
            alias="address",
        )
    )
    carrier: typing.Optional[str] = pydantic.Field(alias="carrier", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    tracking_number: typing.Optional[str] = pydantic.Field(
        alias="tracking_number", default=None
    )
