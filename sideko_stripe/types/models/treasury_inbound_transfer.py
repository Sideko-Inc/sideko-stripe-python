import pydantic
import typing
import typing_extensions

from .treasury_inbound_transfer_metadata import TreasuryInboundTransferMetadata
from .treasury_inbound_transfers_resource_failure_details import (
    TreasuryInboundTransfersResourceFailureDetails,
)
from .treasury_inbound_transfers_resource_inbound_transfer_resource_linked_flows import (
    TreasuryInboundTransfersResourceInboundTransferResourceLinkedFlows,
)
from .treasury_inbound_transfers_resource_inbound_transfer_resource_status_transitions import (
    TreasuryInboundTransfersResourceInboundTransferResourceStatusTransitions,
)

if typing_extensions.TYPE_CHECKING:
    from .inbound_transfers import InboundTransfers
    from .treasury_transaction import TreasuryTransaction


class TreasuryInboundTransfer(pydantic.BaseModel):
    """
    Use [InboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers) to add funds to your [FinancialAccount](https://stripe.com/docs/api#financial_accounts) via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.

    Related guide: [Moving money with Treasury using InboundTransfer objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers)
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
    cancelable: bool = pydantic.Field(
        alias="cancelable",
    )
    """
    Returns `true` if the InboundTransfer is able to be canceled.
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
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    failure_details: typing.Optional[TreasuryInboundTransfersResourceFailureDetails] = (
        pydantic.Field(alias="failure_details", default=None)
    )
    financial_account: str = pydantic.Field(
        alias="financial_account",
    )
    """
    The FinancialAccount that received the funds.
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
    linked_flows: TreasuryInboundTransfersResourceInboundTransferResourceLinkedFlows = (
        pydantic.Field(
            alias="linked_flows",
        )
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: TreasuryInboundTransferMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["treasury.inbound_transfer"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    origin_payment_method: typing.Optional[str] = pydantic.Field(
        alias="origin_payment_method", default=None
    )
    """
    The origin payment method to be debited for an InboundTransfer.
    """
    origin_payment_method_details: typing.Optional["InboundTransfers"] = pydantic.Field(
        alias="origin_payment_method_details", default=None
    )
    returned: typing.Optional[bool] = pydantic.Field(alias="returned", default=None)
    """
    Returns `true` if the funds for an InboundTransfer were returned after the InboundTransfer went to the `succeeded` state.
    """
    statement_descriptor: str = pydantic.Field(
        alias="statement_descriptor",
    )
    """
    Statement descriptor shown when funds are debited from the source. Not all payment networks support `statement_descriptor`.
    """
    status: typing_extensions.Literal[
        "canceled", "failed", "processing", "succeeded"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Status of the InboundTransfer: `processing`, `succeeded`, `failed`, and `canceled`. An InboundTransfer is `processing` if it is created and pending. The status changes to `succeeded` once the funds have been "confirmed" and a `transaction` is created and posted. The status changes to `failed` if the transfer fails.
    """
    status_transitions: TreasuryInboundTransfersResourceInboundTransferResourceStatusTransitions = pydantic.Field(
        alias="status_transitions",
    )
    transaction: typing.Optional[typing.Union[str, "TreasuryTransaction"]] = (
        pydantic.Field(alias="transaction", default=None)
    )
    """
    The Transaction associated with this object.
    """
