import pydantic
import typing_extensions


class PaymentMethodCreateBodyAuBecsDebit(typing_extensions.TypedDict):
    """
    If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
    """

    account_number: typing_extensions.Required[str]

    bsb_number: typing_extensions.Required[str]


class _SerializerPaymentMethodCreateBodyAuBecsDebit(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyAuBecsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_number: str = pydantic.Field(
        alias="account_number",
    )
    bsb_number: str = pydantic.Field(
        alias="bsb_number",
    )
