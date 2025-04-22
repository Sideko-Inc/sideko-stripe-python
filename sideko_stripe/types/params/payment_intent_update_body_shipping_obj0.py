import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_shipping_obj0_address import (
    PaymentIntentUpdateBodyShippingObj0Address,
    _SerializerPaymentIntentUpdateBodyShippingObj0Address,
)


class PaymentIntentUpdateBodyShippingObj0(typing_extensions.TypedDict):
    """
    PaymentIntentUpdateBodyShippingObj0
    """

    address: typing_extensions.Required[PaymentIntentUpdateBodyShippingObj0Address]

    carrier: typing_extensions.NotRequired[str]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[str]

    tracking_number: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentUpdateBodyShippingObj0(pydantic.BaseModel):
    """
    Serializer for PaymentIntentUpdateBodyShippingObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerPaymentIntentUpdateBodyShippingObj0Address = pydantic.Field(
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
