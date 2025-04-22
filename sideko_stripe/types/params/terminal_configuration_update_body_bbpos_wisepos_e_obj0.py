import pydantic
import typing
import typing_extensions


class TerminalConfigurationUpdateBodyBbposWiseposEObj0(typing_extensions.TypedDict):
    """
    TerminalConfigurationUpdateBodyBbposWiseposEObj0
    """

    splashscreen: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerTerminalConfigurationUpdateBodyBbposWiseposEObj0(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationUpdateBodyBbposWiseposEObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    splashscreen: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="splashscreen", default=None
    )
