import pydantic
import typing
import typing_extensions


class TestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetailsUsBankAccount(
    typing_extensions.TypedDict
):
    """
    TestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetailsUsBankAccount
    """

    account_holder_name: typing_extensions.NotRequired[str]

    account_number: typing_extensions.NotRequired[str]

    routing_number: typing_extensions.NotRequired[str]


class _SerializerTestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetailsUsBankAccount(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryReceivedDebitCreateBodyInitiatingPaymentMethodDetailsUsBankAccount handling case conversions
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
