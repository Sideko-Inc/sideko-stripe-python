import pydantic
import typing
import typing_extensions

from .source_update_body_mandate import (
    SourceUpdateBodyMandate,
    _SerializerSourceUpdateBodyMandate,
)
from .source_update_body_metadata_obj0 import (
    SourceUpdateBodyMetadataObj0,
    _SerializerSourceUpdateBodyMetadataObj0,
)
from .source_update_body_owner import (
    SourceUpdateBodyOwner,
    _SerializerSourceUpdateBodyOwner,
)
from .source_update_body_source_order import (
    SourceUpdateBodySourceOrder,
    _SerializerSourceUpdateBodySourceOrder,
)


class SourceUpdateBody(typing_extensions.TypedDict, total=False):
    """
    SourceUpdateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    Amount associated with the source.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    mandate: typing_extensions.NotRequired[SourceUpdateBodyMandate]
    """
    Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[SourceUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    owner: typing_extensions.NotRequired[SourceUpdateBodyOwner]
    """
    Information about the owner of the payment instrument that may be used or required by particular source types.
    """

    source_order: typing_extensions.NotRequired[SourceUpdateBodySourceOrder]
    """
    Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.
    """


class _SerializerSourceUpdateBody(pydantic.BaseModel):
    """
    Serializer for SourceUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    mandate: typing.Optional[_SerializerSourceUpdateBodyMandate] = pydantic.Field(
        alias="mandate", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerSourceUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    owner: typing.Optional[_SerializerSourceUpdateBodyOwner] = pydantic.Field(
        alias="owner", default=None
    )
    source_order: typing.Optional[_SerializerSourceUpdateBodySourceOrder] = (
        pydantic.Field(alias="source_order", default=None)
    )
