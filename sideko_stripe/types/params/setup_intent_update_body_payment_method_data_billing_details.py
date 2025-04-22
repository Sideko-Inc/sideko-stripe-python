import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_data_billing_details_address_obj0 import (
    SetupIntentUpdateBodyPaymentMethodDataBillingDetailsAddressObj0,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataBillingDetailsAddressObj0,
)


class SetupIntentUpdateBodyPaymentMethodDataBillingDetails(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodDataBillingDetails
    """

    address: typing_extensions.NotRequired[
        typing.Union[
            SetupIntentUpdateBodyPaymentMethodDataBillingDetailsAddressObj0, str
        ]
    ]

    email: typing_extensions.NotRequired[typing.Union[str, str]]

    name: typing_extensions.NotRequired[typing.Union[str, str]]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerSetupIntentUpdateBodyPaymentMethodDataBillingDetails(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodDataBillingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[
            _SerializerSetupIntentUpdateBodyPaymentMethodDataBillingDetailsAddressObj0,
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
