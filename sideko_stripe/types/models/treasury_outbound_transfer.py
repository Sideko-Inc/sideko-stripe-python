import pydantic
import typing
import typing_extensions

from .treasury_outbound_transfer_metadata import TreasuryOutboundTransferMetadata
from .treasury_outbound_transfers_resource_outbound_transfer_resource_tracking_details import (
    TreasuryOutboundTransfersResourceOutboundTransferResourceTrackingDetails,
)
from .treasury_outbound_transfers_resource_status_transitions import (
    TreasuryOutboundTransfersResourceStatusTransitions,
)

if typing_extensions.TYPE_CHECKING:
    from .outbound_transfers_payment_method_details import (
        OutboundTransfersPaymentMethodDetails,
    )
    from .treasury_outbound_transfers_resource_returned_details import (
        TreasuryOutboundTransfersResourceReturnedDetails,
    )
    from .treasury_transaction import TreasuryTransaction


class TreasuryOutboundTransfer(pydantic.BaseModel):
    """
    Use [OutboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-transfers) to transfer funds from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) to a PaymentMethod belonging to the same entity. To send funds to a different party, use [OutboundPayments](https://stripe.com/docs/api#outbound_payments) instead. You can send funds over ACH rails or through a domestic wire transfer to a user's own external bank account.

    Simulate OutboundTransfer state changes with the `/v1/test_helpers/treasury/outbound_transfers` endpoints. These methods can only be called on test mode objects.

    Related guide: [Moving money with Treasury using OutboundTransfer objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-transfers)
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
    Returns `true` if the object can be canceled, and `false` otherwise.
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
    destination_payment_method: typing.Optional[str] = pydantic.Field(
        alias="destination_payment_method", default=None
    )
    """
    The PaymentMethod used as the payment instrument for an OutboundTransfer.
    """
    destination_payment_method_details: "OutboundTransfersPaymentMethodDetails" = (
        pydantic.Field(
            alias="destination_payment_method_details",
        )
    )
    expected_arrival_date: int = pydantic.Field(
        alias="expected_arrival_date",
    )
    """
    The date when funds are expected to arrive in the destination account.
    """
    financial_account: str = pydantic.Field(
        alias="financial_account",
    )
    """
    The FinancialAccount that funds were pulled from.
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
    metadata: TreasuryOutboundTransferMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["treasury.outbound_transfer"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    returned_details: typing.Optional[
        "TreasuryOutboundTransfersResourceReturnedDetails"
    ] = pydantic.Field(alias="returned_details", default=None)
    statement_descriptor: str = pydantic.Field(
        alias="statement_descriptor",
    )
    """
    Information about the OutboundTransfer to be sent to the recipient account.
    """
    status: typing_extensions.Literal[
        "canceled", "failed", "posted", "processing", "returned"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Current status of the OutboundTransfer: `processing`, `failed`, `canceled`, `posted`, `returned`. An OutboundTransfer is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundTransfer has been "confirmed" and funds have left the account, or to `failed` or `canceled`. If an OutboundTransfer fails to arrive at its destination, its status will change to `returned`.
    """
    status_transitions: TreasuryOutboundTransfersResourceStatusTransitions = (
        pydantic.Field(
            alias="status_transitions",
        )
    )
    tracking_details: typing.Optional[
        TreasuryOutboundTransfersResourceOutboundTransferResourceTrackingDetails
    ] = pydantic.Field(alias="tracking_details", default=None)
    transaction: typing.Union[str, "TreasuryTransaction"] = pydantic.Field(
        alias="transaction",
    )
    """
    The Transaction associated with this object.
    """
