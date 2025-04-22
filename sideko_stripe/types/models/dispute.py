import pydantic
import typing
import typing_extensions

from .dispute_evidence_details import DisputeEvidenceDetails
from .dispute_metadata import DisputeMetadata
from .dispute_payment_method_details import DisputePaymentMethodDetails

if typing_extensions.TYPE_CHECKING:
    from .balance_transaction import BalanceTransaction
    from .charge import Charge
    from .dispute_evidence import DisputeEvidence
    from .payment_intent import PaymentIntent


class Dispute(pydantic.BaseModel):
    """
    A dispute occurs when a customer questions your charge with their card issuer.
    When this happens, you have the opportunity to respond to the dispute with
    evidence that shows that the charge is legitimate.

    Related guide: [Disputes and fraud](https://stripe.com/docs/disputes)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Disputed amount. Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed).
    """
    balance_transactions: typing.List["BalanceTransaction"] = pydantic.Field(
        alias="balance_transactions",
    )
    """
    List of zero, one, or two balance transactions that show funds withdrawn and reinstated to your Stripe account as a result of this dispute.
    """
    charge: typing.Union[str, "Charge"] = pydantic.Field(
        alias="charge",
    )
    """
    ID of the charge that's disputed.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    enhanced_eligibility_types: typing.List[
        typing_extensions.Literal["visa_compelling_evidence_3"]
    ] = pydantic.Field(
        alias="enhanced_eligibility_types",
    )
    """
    List of eligibility types that are included in `enhanced_evidence`.
    """
    evidence: "DisputeEvidence" = pydantic.Field(
        alias="evidence",
    )
    evidence_details: DisputeEvidenceDetails = pydantic.Field(
        alias="evidence_details",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    is_charge_refundable: bool = pydantic.Field(
        alias="is_charge_refundable",
    )
    """
    If true, it's still possible to refund the disputed payment. After the payment has been fully refunded, no further funds are withdrawn from your Stripe account as a result of this dispute.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: DisputeMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["dispute"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_intent: typing.Optional[typing.Union[str, "PaymentIntent"]] = (
        pydantic.Field(alias="payment_intent", default=None)
    )
    """
    ID of the PaymentIntent that's disputed.
    """
    payment_method_details: typing.Optional[DisputePaymentMethodDetails] = (
        pydantic.Field(alias="payment_method_details", default=None)
    )
    reason: str = pydantic.Field(
        alias="reason",
    )
    """
    Reason given by cardholder for dispute. Possible values are `bank_cannot_process`, `check_returned`, `credit_not_processed`, `customer_initiated`, `debit_not_authorized`, `duplicate`, `fraudulent`, `general`, `incorrect_account_details`, `insufficient_funds`, `product_not_received`, `product_unacceptable`, `subscription_canceled`, or `unrecognized`. Learn more about [dispute reasons](https://stripe.com/docs/disputes/categories).
    """
    status: typing_extensions.Literal[
        "lost",
        "needs_response",
        "under_review",
        "warning_closed",
        "warning_needs_response",
        "warning_under_review",
        "won",
    ] = pydantic.Field(
        alias="status",
    )
    """
    Current status of dispute. Possible values are `warning_needs_response`, `warning_under_review`, `warning_closed`, `needs_response`, `under_review`, `won`, or `lost`.
    """
