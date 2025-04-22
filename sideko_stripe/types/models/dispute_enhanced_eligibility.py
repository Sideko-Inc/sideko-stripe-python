import pydantic
import typing

from .dispute_enhanced_eligibility_visa_compelling_evidence3 import (
    DisputeEnhancedEligibilityVisaCompellingEvidence3,
)
from .dispute_enhanced_eligibility_visa_compliance import (
    DisputeEnhancedEligibilityVisaCompliance,
)


class DisputeEnhancedEligibility(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    visa_compelling_evidence_3: typing.Optional[
        DisputeEnhancedEligibilityVisaCompellingEvidence3
    ] = pydantic.Field(alias="visa_compelling_evidence_3", default=None)
    visa_compliance: typing.Optional[DisputeEnhancedEligibilityVisaCompliance] = (
        pydantic.Field(alias="visa_compliance", default=None)
    )
