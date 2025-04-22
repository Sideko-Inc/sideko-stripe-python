import pydantic
import typing
import typing_extensions

from .file_create_body_file_link_data_metadata_obj0 import (
    FileCreateBodyFileLinkDataMetadataObj0,
    _SerializerFileCreateBodyFileLinkDataMetadataObj0,
)


class FileCreateBodyFileLinkData(typing_extensions.TypedDict):
    """
    Optional parameters that automatically create a [file link](https://stripe.com/docs/api#file_links) for the newly created file.
    """

    create: typing_extensions.Required[bool]

    expires_at: typing_extensions.NotRequired[int]

    metadata: typing_extensions.NotRequired[
        typing.Union[FileCreateBodyFileLinkDataMetadataObj0, str]
    ]


class _SerializerFileCreateBodyFileLinkData(pydantic.BaseModel):
    """
    Serializer for FileCreateBodyFileLinkData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    create: bool = pydantic.Field(
        alias="create",
    )
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    metadata: typing.Optional[
        typing.Union[_SerializerFileCreateBodyFileLinkDataMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
