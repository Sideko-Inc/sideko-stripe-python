import pydantic
import typing_extensions


class PaymentMethodCreateBodySepaDebit(typing_extensions.TypedDict):
    """
    If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
    """

    iban: typing_extensions.Required[str]


class _SerializerPaymentMethodCreateBodySepaDebit(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodySepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    iban: str = pydantic.Field(
        alias="iban",
    )
