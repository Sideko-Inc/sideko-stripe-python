import pydantic
import typing
import typing_extensions

from .test_helper_treasury_received_debit_create_body_initiating_payment_method_details_us_bank_account import (
    TestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetailsUsBankAccount,
    _SerializerTestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetailsUsBankAccount,
)


class TestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetails(
    typing_extensions.TypedDict
):
    """
    Initiating payment method details for the object.
    """

    type_: typing_extensions.Required[typing_extensions.Literal["us_bank_account"]]

    us_bank_account: typing_extensions.NotRequired[
        TestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetailsUsBankAccount
    ]


class _SerializerTestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["us_bank_account"] = pydantic.Field(
        alias="type",
    )
    us_bank_account: typing.Optional[
        _SerializerTestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetailsUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
