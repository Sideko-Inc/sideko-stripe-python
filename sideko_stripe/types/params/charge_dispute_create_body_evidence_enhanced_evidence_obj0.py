import pydantic
import typing
import typing_extensions

from .charge_dispute_create_body_evidence_enhanced_evidence_obj0_visa_compelling_evidence3 import (
    ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3,
    _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3,
)
from .charge_dispute_create_body_evidence_enhanced_evidence_obj0_visa_compliance import (
    ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompliance,
    _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompliance,
)


class ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0(typing_extensions.TypedDict):
    """
    ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0
    """

    visa_compelling_evidence_3: typing_extensions.NotRequired[
        ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3
    ]

    visa_compliance: typing_extensions.NotRequired[
        ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompliance
    ]


class _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0(
    pydantic.BaseModel
):
    """
    Serializer for ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    visa_compelling_evidence_3: typing.Optional[
        _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3
    ] = pydantic.Field(alias="visa_compelling_evidence_3", default=None)
    visa_compliance: typing.Optional[
        _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompliance
    ] = pydantic.Field(alias="visa_compliance", default=None)
