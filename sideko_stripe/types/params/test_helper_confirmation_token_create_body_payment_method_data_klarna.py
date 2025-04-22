import pydantic
import typing
import typing_extensions

from .test_helper_confirmation_token_create_body_payment_method_data_klarna_dob import (
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataKlarnaDob,
    _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataKlarnaDob,
)


class TestHelperConfirmationTokenCreateBodyPaymentMethodDataKlarna(
    typing_extensions.TypedDict
):
    """
    TestHelperConfirmationTokenCreateBodyPaymentMethodDataKlarna
    """

    dob: typing_extensions.NotRequired[
        TestHelperConfirmationTokenCreateBodyPaymentMethodDataKlarnaDob
    ]


class _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataKlarna(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyPaymentMethodDataKlarna handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dob: typing.Optional[
        _SerializerTestHelperConfirmationTokenCreateBodyPaymentMethodDataKlarnaDob
    ] = pydantic.Field(alias="dob", default=None)
