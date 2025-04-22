import pydantic
import typing
import typing_extensions

from .charge_dispute_create_body_evidence_enhanced_evidence_obj0_visa_compelling_evidence3_disputed_transaction import (
    ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction,
    _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction,
)
from .charge_dispute_create_body_evidence_enhanced_evidence_obj0_visa_compelling_evidence3_prior_undisputed_transactions_item import (
    ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem,
    _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem,
)


class ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3(
    typing_extensions.TypedDict
):
    """
    ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3
    """

    disputed_transaction: typing_extensions.NotRequired[
        ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction
    ]

    prior_undisputed_transactions: typing_extensions.NotRequired[
        typing.List[
            ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem
        ]
    ]


class _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3(
    pydantic.BaseModel
):
    """
    Serializer for ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    disputed_transaction: typing.Optional[
        _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction
    ] = pydantic.Field(alias="disputed_transaction", default=None)
    prior_undisputed_transactions: typing.Optional[
        typing.List[
            _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem
        ]
    ] = pydantic.Field(alias="prior_undisputed_transactions", default=None)
