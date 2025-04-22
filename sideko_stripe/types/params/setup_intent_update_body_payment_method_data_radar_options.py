import pydantic
import typing
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodDataRadarOptions(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodDataRadarOptions
    """

    session: typing_extensions.NotRequired[str]


class _SerializerSetupIntentUpdateBodyPaymentMethodDataRadarOptions(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodDataRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
