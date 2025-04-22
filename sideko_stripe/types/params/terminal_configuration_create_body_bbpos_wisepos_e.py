import pydantic
import typing
import typing_extensions


class TerminalConfigurationCreateBodyBbposWiseposE(typing_extensions.TypedDict):
    """
    An object containing device type specific settings for BBPOS WisePOS E readers
    """

    splashscreen: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerTerminalConfigurationCreateBodyBbposWiseposE(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationCreateBodyBbposWiseposE handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    splashscreen: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="splashscreen", default=None
    )
