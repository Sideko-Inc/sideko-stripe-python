import pydantic
import typing
import typing_extensions


class PaymentMethodCreateBodyBacsDebit(typing_extensions.TypedDict):
    """
    If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
    """

    account_number: typing_extensions.NotRequired[str]

    sort_code: typing_extensions.NotRequired[str]


class _SerializerPaymentMethodCreateBodyBacsDebit(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: typing.Optional[str] = pydantic.Field(
        alias="account_number", default=None
    )
    sort_code: typing.Optional[str] = pydantic.Field(alias="sort_code", default=None)
