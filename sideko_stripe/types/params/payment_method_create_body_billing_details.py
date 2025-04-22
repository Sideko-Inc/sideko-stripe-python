import pydantic
import typing
import typing_extensions

from .payment_method_create_body_billing_details_address_obj0 import (
    PaymentMethodCreateBodyBillingDetailsAddressObj0,
    _SerializerPaymentMethodCreateBodyBillingDetailsAddressObj0,
)


class PaymentMethodCreateBodyBillingDetails(typing_extensions.TypedDict):
    """
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    """

    address: typing_extensions.NotRequired[
        typing.Union[PaymentMethodCreateBodyBillingDetailsAddressObj0, str]
    ]

    email: typing_extensions.NotRequired[typing.Union[str, str]]

    name: typing_extensions.NotRequired[typing.Union[str, str]]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerPaymentMethodCreateBodyBillingDetails(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyBillingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[_SerializerPaymentMethodCreateBodyBillingDetailsAddressObj0, str]
    ] = pydantic.Field(alias="address", default=None)
    email: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="email", default=None
    )
    name: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="name", default=None
    )
    phone: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="phone", default=None
    )
