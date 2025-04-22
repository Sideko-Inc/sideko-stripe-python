import pydantic
import typing
import typing_extensions


class TokenCreateBodyBankAccount(typing_extensions.TypedDict):
    """
    The bank account this token will represent.
    """

    account_holder_name: typing_extensions.NotRequired[str]

    account_holder_type: typing_extensions.NotRequired[
        typing_extensions.Literal["company", "individual"]
    ]

    account_number: typing_extensions.Required[str]

    account_type: typing_extensions.NotRequired[
        typing_extensions.Literal["checking", "futsu", "savings", "toza"]
    ]

    country: typing_extensions.Required[str]

    currency: typing_extensions.NotRequired[str]

    payment_method: typing_extensions.NotRequired[str]

    routing_number: typing_extensions.NotRequired[str]


class _SerializerTokenCreateBodyBankAccount(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="account_holder_name", default=None
    )
    account_holder_type: typing.Optional[
        typing_extensions.Literal["company", "individual"]
    ] = pydantic.Field(alias="account_holder_type", default=None)
    account_number: str = pydantic.Field(
        alias="account_number",
    )
    account_type: typing.Optional[
        typing_extensions.Literal["checking", "futsu", "savings", "toza"]
    ] = pydantic.Field(alias="account_type", default=None)
    country: str = pydantic.Field(
        alias="country",
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
