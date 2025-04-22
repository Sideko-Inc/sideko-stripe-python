import pydantic
import typing

from .dispute_enhanced_eligibility import DisputeEnhancedEligibility


class DisputeEvidenceDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    due_by: typing.Optional[int] = pydantic.Field(alias="due_by", default=None)
    """
    Date by which evidence must be submitted in order to successfully challenge dispute. Will be 0 if the customer's bank or credit card company doesn't allow a response for this particular dispute.
    """
    enhanced_eligibility: DisputeEnhancedEligibility = pydantic.Field(
        alias="enhanced_eligibility",
    )
    has_evidence: bool = pydantic.Field(
        alias="has_evidence",
    )
    """
    Whether evidence has been staged for this dispute.
    """
    past_due: bool = pydantic.Field(
        alias="past_due",
    )
    """
    Whether the last evidence submission was submitted past the due date. Defaults to `false` if no evidence submissions have occurred. If `true`, then delivery of the latest evidence is *not* guaranteed.
    """
    submission_count: int = pydantic.Field(
        alias="submission_count",
    )
    """
    The number of times evidence has been submitted. Typically, you may only submit evidence once.
    """
