import pydantic
import typing_extensions


class SetupIntentConfirmBodyPaymentMethodDataSepaDebit(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodDataSepaDebit
    """

    iban: typing_extensions.Required[str]


class _SerializerSetupIntentConfirmBodyPaymentMethodDataSepaDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodDataSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    iban: str = pydantic.Field(
        alias="iban",
    )
