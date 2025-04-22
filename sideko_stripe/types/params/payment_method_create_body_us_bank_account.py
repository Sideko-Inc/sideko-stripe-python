import pydantic
import typing
import typing_extensions


class PaymentMethodCreateBodyUsBankAccount(typing_extensions.TypedDict):
    """
    If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
    """

    account_holder_type: typing_extensions.NotRequired[
        typing_extensions.Literal["company", "individual"]
    ]

    account_number: typing_extensions.NotRequired[str]

    account_type: typing_extensions.NotRequired[
        typing_extensions.Literal["checking", "savings"]
    ]

    financial_connections_account: typing_extensions.NotRequired[str]

    routing_number: typing_extensions.NotRequired[str]


class _SerializerPaymentMethodCreateBodyUsBankAccount(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyUsBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_holder_type: typing.Optional[
        typing_extensions.Literal["company", "individual"]
    ] = pydantic.Field(alias="account_holder_type", default=None)
    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    account_type: typing.Optional[typing_extensions.Literal["checking", "savings"]] = (
        pydantic.Field(alias="account_type", default=None)
    )
    financial_connections_account: typing.Optional[str] = pydantic.Field(
        alias="financial_connections_account", default=None
    )
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
