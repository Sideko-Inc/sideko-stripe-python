import pydantic
import typing_extensions


class SetupIntentConfirmBodyPaymentMethodDataKlarnaDob(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodDataKlarnaDob
    """

    day: typing_extensions.Required[int]

    month: typing_extensions.Required[int]

    year: typing_extensions.Required[int]


class _SerializerSetupIntentConfirmBodyPaymentMethodDataKlarnaDob(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodDataKlarnaDob handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    day: int = pydantic.Field(
        alias="day",
    )
    month: int = pydantic.Field(
        alias="month",
    )
    year: int = pydantic.Field(
        alias="year",
    )
