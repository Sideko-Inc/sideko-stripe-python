import pydantic
import typing
import typing_extensions


class PaymentMethodCreateBodyNzBankAccount(typing_extensions.TypedDict):
    """
    If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.
    """

    account_holder_name: typing_extensions.NotRequired[str]

    account_number: typing_extensions.Required[str]

    bank_code: typing_extensions.Required[str]

    branch_code: typing_extensions.Required[str]

    reference: typing_extensions.NotRequired[str]

    suffix: typing_extensions.Required[str]


class _SerializerPaymentMethodCreateBodyNzBankAccount(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyNzBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="account_holder_name", default=None
    )
    account_number: str = pydantic.Field(
        alias="account_number",
    )
    bank_code: str = pydantic.Field(
        alias="bank_code",
    )
    branch_code: str = pydantic.Field(
        alias="branch_code",
    )
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    suffix: str = pydantic.Field(
        alias="suffix",
    )
