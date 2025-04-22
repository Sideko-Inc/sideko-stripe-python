import pydantic
import typing
import typing_extensions


class FileCreateBodyFileLinkDataMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    FileCreateBodyFileLinkDataMetadataObj0
    """


class _SerializerFileCreateBodyFileLinkDataMetadataObj0(pydantic.BaseModel):
    """
    Serializer for FileCreateBodyFileLinkDataMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
