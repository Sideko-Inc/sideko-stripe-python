import pydantic
import typing
import typing_extensions


class TerminalConfigurationCreateBodyVerifoneP400(typing_extensions.TypedDict):
    """
    An object containing device type specific settings for Verifone P400 readers
    """

    splashscreen: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerTerminalConfigurationCreateBodyVerifoneP400(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationCreateBodyVerifoneP400 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    splashscreen: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="splashscreen", default=None
    )
