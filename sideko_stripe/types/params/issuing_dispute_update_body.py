import pydantic
import typing
import typing_extensions

from .issuing_dispute_update_body_evidence import (
    IssuingDisputeUpdateBodyEvidence,
    _SerializerIssuingDisputeUpdateBodyEvidence,
)
from .issuing_dispute_update_body_metadata_obj0 import (
    IssuingDisputeUpdateBodyMetadataObj0,
    _SerializerIssuingDisputeUpdateBodyMetadataObj0,
)


class IssuingDisputeUpdateBody(typing_extensions.TypedDict, total=False):
    """
    IssuingDisputeUpdateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """

    evidence: typing_extensions.NotRequired[IssuingDisputeUpdateBodyEvidence]
    """
    Evidence provided for the dispute.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerIssuingDisputeUpdateBody(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    evidence: typing.Optional[_SerializerIssuingDisputeUpdateBodyEvidence] = (
        pydantic.Field(alias="evidence", default=None)
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerIssuingDisputeUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
