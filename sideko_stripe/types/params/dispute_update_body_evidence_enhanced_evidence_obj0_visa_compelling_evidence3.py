import pydantic
import typing
import typing_extensions

from .dispute_update_body_evidence_enhanced_evidence_obj0_visa_compelling_evidence3_disputed_transaction import (
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction,
    _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction,
)
from .dispute_update_body_evidence_enhanced_evidence_obj0_visa_compelling_evidence3_prior_undisputed_transactions_item import (
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem,
    _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem,
)


class DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3(
    typing_extensions.TypedDict
):
    """
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3
    """

    disputed_transaction: typing_extensions.NotRequired[
        DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction
    ]

    prior_undisputed_transactions: typing_extensions.NotRequired[
        typing.List[
            DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem
        ]
    ]


class _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3(
    pydantic.BaseModel
):
    """
    Serializer for DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    disputed_transaction: typing.Optional[
        _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction
    ] = pydantic.Field(alias="disputed_transaction", default=None)
    prior_undisputed_transactions: typing.Optional[
        typing.List[
            _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem
        ]
    ] = pydantic.Field(alias="prior_undisputed_transactions", default=None)
