import pydantic
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodDataSepaDebit(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodDataSepaDebit
    """

    iban: typing_extensions.Required[str]


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataSepaDebit(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    iban: str = pydantic.Field(
        alias="iban",
    )
