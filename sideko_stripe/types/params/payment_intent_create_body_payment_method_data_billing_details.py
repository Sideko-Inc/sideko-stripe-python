import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_data_billing_details_address_obj0 import (
    PaymentIntentCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
)


class PaymentIntentCreateBodyPaymentMethodDataBillingDetails(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodDataBillingDetails
    """

    address: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentCreateBodyPaymentMethodDataBillingDetailsAddressObj0, str
        ]
    ]

    email: typing_extensions.NotRequired[typing.Union[str, str]]

    name: typing_extensions.NotRequired[typing.Union[str, str]]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerPaymentIntentCreateBodyPaymentMethodDataBillingDetails(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodDataBillingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
            str,
        ]
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
