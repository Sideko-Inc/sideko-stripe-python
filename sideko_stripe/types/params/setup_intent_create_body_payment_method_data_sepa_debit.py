import pydantic
import typing_extensions


class SetupIntentCreateBodyPaymentMethodDataSepaDebit(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodDataSepaDebit
    """

    iban: typing_extensions.Required[str]


class _SerializerSetupIntentCreateBodyPaymentMethodDataSepaDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodDataSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    iban: str = pydantic.Field(
        alias="iban",
    )
