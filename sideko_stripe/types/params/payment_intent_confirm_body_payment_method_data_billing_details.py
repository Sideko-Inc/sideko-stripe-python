import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_data_billing_details_address_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodDataBillingDetailsAddressObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataBillingDetailsAddressObj0,
)


class PaymentIntentConfirmBodyPaymentMethodDataBillingDetails(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodDataBillingDetails
    """

    address: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentConfirmBodyPaymentMethodDataBillingDetailsAddressObj0, str
        ]
    ]

    email: typing_extensions.NotRequired[typing.Union[str, str]]

    name: typing_extensions.NotRequired[typing.Union[str, str]]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataBillingDetails(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataBillingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodDataBillingDetailsAddressObj0,
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
