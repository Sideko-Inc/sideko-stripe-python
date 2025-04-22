import pydantic
import typing
import typing_extensions


class TerminalConfigurationUpdateBodyVerifoneP400Obj0(typing_extensions.TypedDict):
    """
    TerminalConfigurationUpdateBodyVerifoneP400Obj0
    """

    splashscreen: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerTerminalConfigurationUpdateBodyVerifoneP400Obj0(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationUpdateBodyVerifoneP400Obj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    splashscreen: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="splashscreen", default=None
    )
