import pydantic
import typing
import typing_extensions

from .transfer_update_body_metadata_obj0 import (
    TransferUpdateBodyMetadataObj0,
    _SerializerTransferUpdateBodyMetadataObj0,
)


class TransferUpdateBody(typing_extensions.TypedDict, total=False):
    """
    TransferUpdateBody
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[TransferUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerTransferUpdateBody(pydantic.BaseModel):
    """
    Serializer for TransferUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerTransferUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
