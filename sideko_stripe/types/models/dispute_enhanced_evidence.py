import pydantic
import typing

from .dispute_enhanced_evidence_visa_compelling_evidence3 import (
    DisputeEnhancedEvidenceVisaCompellingEvidence3,
)
from .dispute_enhanced_evidence_visa_compliance import (
    DisputeEnhancedEvidenceVisaCompliance,
)


class DisputeEnhancedEvidence(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    visa_compelling_evidence_3: typing.Optional[
        DisputeEnhancedEvidenceVisaCompellingEvidence3
    ] = pydantic.Field(alias="visa_compelling_evidence_3", default=None)
    visa_compliance: typing.Optional[DisputeEnhancedEvidenceVisaCompliance] = (
        pydantic.Field(alias="visa_compliance", default=None)
    )
