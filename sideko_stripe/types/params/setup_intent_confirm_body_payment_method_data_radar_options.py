import pydantic
import typing
import typing_extensions


class SetupIntentConfirmBodyPaymentMethodDataRadarOptions(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodDataRadarOptions
    """

    session: typing_extensions.NotRequired[str]


class _SerializerSetupIntentConfirmBodyPaymentMethodDataRadarOptions(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodDataRadarOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    session: typing.Optional[str] = pydantic.Field(alias="session", default=None)
