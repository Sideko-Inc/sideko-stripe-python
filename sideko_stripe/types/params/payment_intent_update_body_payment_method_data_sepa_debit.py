import pydantic
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodDataSepaDebit(typing_extensions.TypedDict):
    """
    PaymentIntentUpdateBodyPaymentMethodDataSepaDebit
    """

    iban: typing_extensions.Required[str]


class _SerializerPaymentIntentUpdateBodyPaymentMethodDataSepaDebit(pydantic.BaseModel):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodDataSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    iban: str = pydantic.Field(
        alias="iban",
    )
