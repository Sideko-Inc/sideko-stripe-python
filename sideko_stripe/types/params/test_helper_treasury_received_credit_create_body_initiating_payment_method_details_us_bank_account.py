import pydantic
import typing
import typing_extensions


class TestHelperTreasuryReceivedCreditCreateBodyInitiatingPaymentMethodDetailsUsBankAccount(
    typing_extensions.TypedDict
):
    """
    TestHelperTreasuryReceivedCreditCreateBodyInitiatingPaymentMethodDetailsUsBankAccount
    """

    account_holder_name: typing_extensions.NotRequired[str]

    account_number: typing_extensions.NotRequired[str]

    routing_number: typing_extensions.NotRequired[str]


class _SerializerTestHelperTreasuryReceivedCreditCreateBodyInitiatingPaymentMethodDetailsUsBankAccount(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryReceivedCreditCreateBodyInitiatingPaymentMethodDetailsUsBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="account_holder_name", default=None
    )
    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
