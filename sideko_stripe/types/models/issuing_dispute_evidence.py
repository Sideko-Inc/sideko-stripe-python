import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .issuing_dispute_canceled_evidence import IssuingDisputeCanceledEvidence
    from .issuing_dispute_duplicate_evidence import IssuingDisputeDuplicateEvidence
    from .issuing_dispute_fraudulent_evidence import IssuingDisputeFraudulentEvidence
    from .issuing_dispute_merchandise_not_as_described_evidence import (
        IssuingDisputeMerchandiseNotAsDescribedEvidence,
    )
    from .issuing_dispute_no_valid_authorization_evidence import (
        IssuingDisputeNoValidAuthorizationEvidence,
    )
    from .issuing_dispute_not_received_evidence import IssuingDisputeNotReceivedEvidence
    from .issuing_dispute_other_evidence import IssuingDisputeOtherEvidence
    from .issuing_dispute_service_not_as_described_evidence import (
        IssuingDisputeServiceNotAsDescribedEvidence,
    )


class IssuingDisputeEvidence(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    canceled: typing.Optional["IssuingDisputeCanceledEvidence"] = pydantic.Field(
        alias="canceled", default=None
    )
    duplicate: typing.Optional["IssuingDisputeDuplicateEvidence"] = pydantic.Field(
        alias="duplicate", default=None
    )
    fraudulent: typing.Optional["IssuingDisputeFraudulentEvidence"] = pydantic.Field(
        alias="fraudulent", default=None
    )
    merchandise_not_as_described: typing.Optional[
        "IssuingDisputeMerchandiseNotAsDescribedEvidence"
    ] = pydantic.Field(alias="merchandise_not_as_described", default=None)
    no_valid_authorization: typing.Optional[
        "IssuingDisputeNoValidAuthorizationEvidence"
    ] = pydantic.Field(alias="no_valid_authorization", default=None)
    not_received: typing.Optional["IssuingDisputeNotReceivedEvidence"] = pydantic.Field(
        alias="not_received", default=None
    )
    other: typing.Optional["IssuingDisputeOtherEvidence"] = pydantic.Field(
        alias="other", default=None
    )
    reason: typing_extensions.Literal[
        "canceled",
        "duplicate",
        "fraudulent",
        "merchandise_not_as_described",
        "no_valid_authorization",
        "not_received",
        "other",
        "service_not_as_described",
    ] = pydantic.Field(
        alias="reason",
    )
    """
    The reason for filing the dispute. Its value will match the field containing the evidence.
    """
    service_not_as_described: typing.Optional[
        "IssuingDisputeServiceNotAsDescribedEvidence"
    ] = pydantic.Field(alias="service_not_as_described", default=None)
