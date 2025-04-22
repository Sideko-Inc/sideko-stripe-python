import pydantic
import typing
import typing_extensions


class SetupIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline(
    typing_extensions.TypedDict
):
    """
    SetupIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline
    """

    ip_address: typing_extensions.NotRequired[str]

    user_agent: typing_extensions.NotRequired[str]


class _SerializerSetupIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    user_agent: typing.Optional[str] = pydantic.Field(alias="user_agent", default=None)
