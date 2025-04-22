import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_payment_method_data_billing_details_address_obj0 import (
    SetupIntentCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
    _SerializerSetupIntentCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
)


class SetupIntentCreateBodyPaymentMethodDataBillingDetails(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodDataBillingDetails
    """

    address: typing_extensions.NotRequired[
        typing.Union[
            SetupIntentCreateBodyPaymentMethodDataBillingDetailsAddressObj0, str
        ]
    ]

    email: typing_extensions.NotRequired[typing.Union[str, str]]

    name: typing_extensions.NotRequired[typing.Union[str, str]]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerSetupIntentCreateBodyPaymentMethodDataBillingDetails(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodDataBillingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[
            _SerializerSetupIntentCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
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
