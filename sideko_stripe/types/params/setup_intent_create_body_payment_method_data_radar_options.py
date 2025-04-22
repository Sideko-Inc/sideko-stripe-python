import pydantic
import typing
import typing_extensions


class SetupIntentCreateBodyPaymentMethodDataRadarOptions(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodDataRadarOptions
    """

    session: typing_extensions.NotRequired[str]


class _SerializerSetupIntentCreateBodyPaymentMethodDataRadarOptions(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodDataRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
