import pydantic
import typing
import typing_extensions

from .test_helper_confirmation_token_create_body_payment_method_data_billing_details_address_obj0 import (
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
    _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
)


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataBillingDetails(
    typing_extensions.TypedDict
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataBillingDetails
    """

    address: typing_extensions.NotRequired[
        typing.Union[
            TestHelperConfirmationTokenCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
            str,
        ]
    ]

    email: typing_extensions.NotRequired[typing.Union[str, str]]

    name: typing_extensions.NotRequired[typing.Union[str, str]]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataBillingDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataBillingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[
            _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataBillingDetailsAddressObj0,
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
