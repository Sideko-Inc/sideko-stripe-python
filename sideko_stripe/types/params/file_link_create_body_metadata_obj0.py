import pydantic
import typing
import typing_extensions


class FileLinkCreateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    FileLinkCreateBodyMetadataObj0
    """


class _SerializerFileLinkCreateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for FileLinkCreateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
