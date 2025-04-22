import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_data_billing_details_address_obj0 import (
    SetupIntentConfirmBodyPaymentMethodDataBillingDetailsAddressObj0,
    _SerializerSetupIntentConfirmBodyPaymentMethodDataBillingDetailsAddressObj0,
)


class SetupIntentConfirmBodyPaymentMethodDataBillingDetails(
    typing_extensions.TypedDict
):
    """
    SetupIntentConfirmBodyPaymentMethodDataBillingDetails
    """

    address: typing_extensions.NotRequired[
        typing.Union[
            SetupIntentConfirmBodyPaymentMethodDataBillingDetailsAddressObj0, str
        ]
    ]

    email: typing_extensions.NotRequired[typing.Union[str, str]]

    name: typing_extensions.NotRequired[typing.Union[str, str]]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerSetupIntentConfirmBodyPaymentMethodDataBillingDetails(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodDataBillingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[
            _SerializerSetupIntentConfirmBodyPaymentMethodDataBillingDetailsAddressObj0,
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
