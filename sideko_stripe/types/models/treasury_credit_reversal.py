import pydantic
import typing
import typing_extensions

from .treasury_credit_reversal_metadata import TreasuryCreditReversalMetadata
from .treasury_received_credits_resource_status_transitions import (
    TreasuryReceivedCreditsResourceStatusTransitions,
)

if typing_extensions.TYPE_CHECKING:
    from .treasury_transaction import TreasuryTransaction


class TreasuryCreditReversal(pydantic.BaseModel):
    """
    You can reverse some [ReceivedCredits](https://stripe.com/docs/api#received_credits) depending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount (in cents) transferred.
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
    financial_account: str = pydantic.Field(
        alias="financial_account",
    )
    """
    The FinancialAccount to reverse funds from.
    """
    hosted_regulatory_receipt_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_regulatory_receipt_url", default=None
    )
    """
    A [hosted transaction receipt](https://stripe.com/docs/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses.
    """
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
    metadata: TreasuryCreditReversalMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    network: typing_extensions.Literal["ach", "stripe"] = pydantic.Field(
        alias="network",
    )
    """
    The rails used to reverse the funds.
    """
    object: typing_extensions.Literal["treasury.credit_reversal"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    received_credit: str = pydantic.Field(
        alias="received_credit",
    )
    """
    The ReceivedCredit being reversed.
    """
    status: typing_extensions.Literal["canceled", "posted", "processing"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    Status of the CreditReversal
    """
    status_transitions: TreasuryReceivedCreditsResourceStatusTransitions = (
        pydantic.Field(
            alias="status_transitions",
        )
    )
    transaction: typing.Optional[typing.Union[str, "TreasuryTransaction"]] = (
        pydantic.Field(alias="transaction", default=None)
    )
    """
    The Transaction associated with this object.
    """
