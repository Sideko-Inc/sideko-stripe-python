import pydantic
import typing
import typing_extensions


class TerminalLocationCreateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    TerminalLocationCreateBodyMetadataObj0
    """


class _SerializerTerminalLocationCreateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for TerminalLocationCreateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
