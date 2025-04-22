import pydantic
import typing
import typing_extensions

from .dispute_update_body_evidence import (
    DisputeUpdateBodyEvidence,
    _SerializerDisputeUpdateBodyEvidence,
)
from .dispute_update_body_metadata_obj0 import (
    DisputeUpdateBodyMetadataObj0,
    _SerializerDisputeUpdateBodyMetadataObj0,
)


class DisputeUpdateBody(typing_extensions.TypedDict, total=False):
    """
    DisputeUpdateBody
    """

    evidence: typing_extensions.NotRequired[DisputeUpdateBodyEvidence]
    """
    Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[DisputeUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    submit: typing_extensions.NotRequired[bool]
    """
    Whether to immediately submit evidence to the bank. If `false`, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to `true` (the default).
    """


class _SerializerDisputeUpdateBody(pydantic.BaseModel):
    """
    Serializer for DisputeUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    evidence: typing.Optional[_SerializerDisputeUpdateBodyEvidence] = pydantic.Field(
        alias="evidence", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerDisputeUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    submit: typing.Optional[bool] = pydantic.Field(alias="submit", default=None)
