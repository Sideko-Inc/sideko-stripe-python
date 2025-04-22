import pydantic
import typing
import typing_extensions

from .issuing_dispute_create_body_evidence import (
    IssuingDisputeCreateBodyEvidence,
    _SerializerIssuingDisputeCreateBodyEvidence,
)
from .issuing_dispute_create_body_metadata import (
    IssuingDisputeCreateBodyMetadata,
    _SerializerIssuingDisputeCreateBodyMetadata,
)
from .issuing_dispute_create_body_treasury import (
    IssuingDisputeCreateBodyTreasury,
    _SerializerIssuingDisputeCreateBodyTreasury,
)


class IssuingDisputeCreateBody(typing_extensions.TypedDict, total=False):
    """
    IssuingDisputeCreateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If not set, defaults to the full transaction amount.
    """

    evidence: typing_extensions.NotRequired[IssuingDisputeCreateBodyEvidence]
    """
    Evidence provided for the dispute.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[IssuingDisputeCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    transaction: typing_extensions.NotRequired[str]
    """
    The ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, use `treasury.received_debit`.
    """

    treasury: typing_extensions.NotRequired[IssuingDisputeCreateBodyTreasury]
    """
    Params for disputes related to Treasury FinancialAccounts
    """


class _SerializerIssuingDisputeCreateBody(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    evidence: typing.Optional[_SerializerIssuingDisputeCreateBodyEvidence] = (
        pydantic.Field(alias="evidence", default=None)
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerIssuingDisputeCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    transaction: typing.Optional[str] = pydantic.Field(
        alias="transaction", default=None
    )
    treasury: typing.Optional[_SerializerIssuingDisputeCreateBodyTreasury] = (
        pydantic.Field(alias="treasury", default=None)
    )
