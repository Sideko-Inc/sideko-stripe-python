import pydantic
import typing

from .dispute_visa_compelling_evidence3_disputed_transaction import (
    DisputeVisaCompellingEvidence3DisputedTransaction,
)
from .dispute_visa_compelling_evidence3_prior_undisputed_transaction import (
    DisputeVisaCompellingEvidence3PriorUndisputedTransaction,
)


class DisputeEnhancedEvidenceVisaCompellingEvidence3(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disputed_transaction: typing.Optional[
        DisputeVisaCompellingEvidence3DisputedTransaction
    ] = pydantic.Field(alias="disputed_transaction", default=None)
    prior_undisputed_transactions: typing.List[
        DisputeVisaCompellingEvidence3PriorUndisputedTransaction
    ] = pydantic.Field(
        alias="prior_undisputed_transactions",
    )
    """
    List of exactly two prior undisputed transaction objects for Visa Compelling Evidence 3.0 evidence submission.
    """
