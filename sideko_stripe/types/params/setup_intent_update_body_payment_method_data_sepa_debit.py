import pydantic
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodDataSepaDebit(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodDataSepaDebit
    """

    iban: typing_extensions.Required[str]


class _SerializerSetupIntentUpdateBodyPaymentMethodDataSepaDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodDataSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    iban: str = pydantic.Field(
        alias="iban",
    )
