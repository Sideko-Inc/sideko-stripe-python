import pydantic
import typing
import typing_extensions

from .dispute_update_body_evidence_enhanced_evidence_obj0_visa_compelling_evidence3 import (
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3,
    _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3,
)
from .dispute_update_body_evidence_enhanced_evidence_obj0_visa_compliance import (
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompliance,
    _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompliance,
)


class DisputeUpdateBodyEvidenceEnhancedEvidenceObj0(typing_extensions.TypedDict):
    """
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0
    """

    visa_compelling_evidence_3: typing_extensions.NotRequired[
        DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3
    ]

    visa_compliance: typing_extensions.NotRequired[
        DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompliance
    ]


class _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0(pydantic.BaseModel):
    """
    Serializer for DisputeUpdateBodyEvidenceEnhancedEvidenceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    visa_compelling_evidence_3: typing.Optional[
        _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3
    ] = pydantic.Field(alias="visa_compelling_evidence_3", default=None)
    visa_compliance: typing.Optional[
        _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompliance
    ] = pydantic.Field(alias="visa_compliance", default=None)
