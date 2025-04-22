import pydantic
import typing
import typing_extensions

from .treasury_outbound_payment_metadata import TreasuryOutboundPaymentMetadata
from .treasury_outbound_payments_resource_outbound_payment_resource_end_user_details import (
    TreasuryOutboundPaymentsResourceOutboundPaymentResourceEndUserDetails,
)
from .treasury_outbound_payments_resource_outbound_payment_resource_status_transitions import (
    TreasuryOutboundPaymentsResourceOutboundPaymentResourceStatusTransitions,
)
from .treasury_outbound_payments_resource_outbound_payment_resource_tracking_details import (
    TreasuryOutboundPaymentsResourceOutboundPaymentResourceTrackingDetails,
)

if typing_extensions.TYPE_CHECKING:
    from .outbound_payments_payment_method_details import (
        OutboundPaymentsPaymentMethodDetails,
    )
    from .treasury_outbound_payments_resource_returned_status import (
        TreasuryOutboundPaymentsResourceReturnedStatus,
    )
    from .treasury_transaction import TreasuryTransaction


class TreasuryOutboundPayment(pydantic.BaseModel):
    """
    Use [OutboundPayments](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-payments) to send funds to another party's external bank account or [FinancialAccount](https://stripe.com/docs/api#financial_accounts). To send money to an account belonging to the same user, use an [OutboundTransfer](https://stripe.com/docs/api#outbound_transfers).

    Simulate OutboundPayment state changes with the `/v1/test_helpers/treasury/outbound_payments` endpoints. These methods can only be called on test mode objects.

    Related guide: [Moving money with Treasury using OutboundPayment objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-payments)
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
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    """
    ID of the [customer](https://stripe.com/docs/api/customers) to whom an OutboundPayment is sent.
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
    The PaymentMethod via which an OutboundPayment is sent. This field can be empty if the OutboundPayment was created using `destination_payment_method_data`.
    """
    destination_payment_method_details: typing.Optional[
        "OutboundPaymentsPaymentMethodDetails"
    ] = pydantic.Field(alias="destination_payment_method_details", default=None)
    end_user_details: typing.Optional[
        TreasuryOutboundPaymentsResourceOutboundPaymentResourceEndUserDetails
    ] = pydantic.Field(alias="end_user_details", default=None)
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
    metadata: TreasuryOutboundPaymentMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["treasury.outbound_payment"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    returned_details: typing.Optional[
        "TreasuryOutboundPaymentsResourceReturnedStatus"
    ] = pydantic.Field(alias="returned_details", default=None)
    statement_descriptor: str = pydantic.Field(
        alias="statement_descriptor",
    )
    """
    The description that appears on the receiving end for an OutboundPayment (for example, bank statement for external bank transfer).
    """
    status: typing_extensions.Literal[
        "canceled", "failed", "posted", "processing", "returned"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Current status of the OutboundPayment: `processing`, `failed`, `posted`, `returned`, `canceled`. An OutboundPayment is `processing` if it has been created and is pending. The status changes to `posted` once the OutboundPayment has been "confirmed" and funds have left the account, or to `failed` or `canceled`. If an OutboundPayment fails to arrive at its destination, its status will change to `returned`.
    """
    status_transitions: TreasuryOutboundPaymentsResourceOutboundPaymentResourceStatusTransitions = pydantic.Field(
        alias="status_transitions",
    )
    tracking_details: typing.Optional[
        TreasuryOutboundPaymentsResourceOutboundPaymentResourceTrackingDetails
    ] = pydantic.Field(alias="tracking_details", default=None)
    transaction: typing.Union[str, "TreasuryTransaction"] = pydantic.Field(
        alias="transaction",
    )
    """
    The Transaction associated with this object.
    """
