import pydantic
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodDataSepaDebit(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodDataSepaDebit
    """

    iban: typing_extensions.Required[str]


class _SerializerPaymentIntentCreateBodyPaymentMethodDataSepaDebit(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodDataSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    iban: str = pydantic.Field(
        alias="iban",
    )
