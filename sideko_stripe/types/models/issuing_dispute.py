import pydantic
import typing
import typing_extensions

from .issuing_dispute_metadata import IssuingDisputeMetadata
from .issuing_dispute_treasury import IssuingDisputeTreasury

if typing_extensions.TYPE_CHECKING:
    from .balance_transaction import BalanceTransaction
    from .issuing_dispute_evidence import IssuingDisputeEvidence
    from .issuing_transaction import IssuingTransaction


class IssuingDispute(pydantic.BaseModel):
    """
    As a [card issuer](https://stripe.com/docs/issuing), you can dispute transactions that the cardholder does not recognize, suspects to be fraudulent, or has other issues with.

    Related guide: [Issuing disputes](https://stripe.com/docs/issuing/purchases/disputes)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Disputed amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). Usually the amount of the `transaction`, but can differ (usually because of currency fluctuation).
    """
    balance_transactions: typing.Optional[typing.List["BalanceTransaction"]] = (
        pydantic.Field(alias="balance_transactions", default=None)
    )
    """
    List of balance transactions associated with the dispute.
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
    The currency the `transaction` was made in.
    """
    evidence: "IssuingDisputeEvidence" = pydantic.Field(
        alias="evidence",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    loss_reason: typing.Optional[
        typing_extensions.Literal[
            "cardholder_authentication_issuer_liability",
            "eci5_token_transaction_with_tavv",
            "excess_disputes_in_timeframe",
            "has_not_met_the_minimum_dispute_amount_requirements",
            "invalid_duplicate_dispute",
            "invalid_incorrect_amount_dispute",
            "invalid_no_authorization",
            "invalid_use_of_disputes",
            "merchandise_delivered_or_shipped",
            "merchandise_or_service_as_described",
            "not_cancelled",
            "other",
            "refund_issued",
            "submitted_beyond_allowable_time_limit",
            "transaction_3ds_required",
            "transaction_approved_after_prior_fraud_dispute",
            "transaction_authorized",
            "transaction_electronically_read",
            "transaction_qualifies_for_visa_easy_payment_service",
            "transaction_unattended",
        ]
    ] = pydantic.Field(alias="loss_reason", default=None)
    """
    The enum that describes the dispute loss outcome. If the dispute is not lost, this field will be absent. New enum values may be added in the future, so be sure to handle unknown values.
    """
    metadata: IssuingDisputeMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["issuing.dispute"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal[
        "expired", "lost", "submitted", "unsubmitted", "won"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Current status of the dispute.
    """
    transaction: typing.Union[str, "IssuingTransaction"] = pydantic.Field(
        alias="transaction",
    )
    """
    The transaction being disputed.
    """
    treasury: typing.Optional[IssuingDisputeTreasury] = pydantic.Field(
        alias="treasury", default=None
    )
