import pydantic
import typing
import typing_extensions

from .file_link_update_body_metadata_obj0 import (
    FileLinkUpdateBodyMetadataObj0,
    _SerializerFileLinkUpdateBodyMetadataObj0,
)


class FileLinkUpdateBody(typing_extensions.TypedDict, total=False):
    """
    FileLinkUpdateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["now"], int, str]
    ]
    """
    A future timestamp after which the link will no longer be usable, or `now` to expire the link immediately.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[FileLinkUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerFileLinkUpdateBody(pydantic.BaseModel):
    """
    Serializer for FileLinkUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    expires_at: typing.Optional[
        typing.Union[typing_extensions.Literal["now"], int, str]
    ] = pydantic.Field(alias="expires_at", default=None)
    metadata: typing.Optional[
        typing.Union[_SerializerFileLinkUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
