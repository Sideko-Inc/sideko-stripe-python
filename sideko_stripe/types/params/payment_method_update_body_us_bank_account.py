import pydantic
import typing
import typing_extensions


class PaymentMethodUpdateBodyUsBankAccount(typing_extensions.TypedDict):
    """
    If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
    """

    account_holder_type: typing_extensions.NotRequired[
        typing_extensions.Literal["company", "individual"]
    ]

    account_type: typing_extensions.NotRequired[
        typing_extensions.Literal["checking", "savings"]
    ]


class _SerializerPaymentMethodUpdateBodyUsBankAccount(pydantic.BaseModel):
    """
    Serializer for PaymentMethodUpdateBodyUsBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_holder_type: typing.Optional[
        typing_extensions.Literal["company", "individual"]
    ] = pydantic.Field(alias="account_holder_type", default=None)
    account_type: typing.Optional[typing_extensions.Literal["checking", "savings"]] = (
        pydantic.Field(alias="account_type", default=None)
    )
