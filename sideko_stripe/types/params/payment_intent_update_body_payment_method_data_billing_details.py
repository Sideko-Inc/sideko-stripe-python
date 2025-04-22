import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_payment_method_data_billing_details_address_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodDataBillingDetailsAddressObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodDataBillingDetailsAddressObj0,
)


class PaymentIntentUpdateBodyPaymentMethodDataBillingDetails(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodDataBillingDetails
    """

    address: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentUpdateBodyPaymentMethodDataBillingDetailsAddressObj0, str
        ]
    ]

    email: typing_extensions.NotRequired[typing.Union[str, str]]

    name: typing_extensions.NotRequired[typing.Union[str, str]]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerPaymentIntentUpdateBodyPaymentMethodDataBillingDetails(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodDataBillingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodDataBillingDetailsAddressObj0,
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
