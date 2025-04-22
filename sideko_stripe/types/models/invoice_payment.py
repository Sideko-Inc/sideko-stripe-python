import pydantic
import typing
import typing_extensions

from .deleted_invoice import DeletedInvoice
from .invoices_payments_invoice_payment_status_transitions import (
    InvoicesPaymentsInvoicePaymentStatusTransitions,
)

if typing_extensions.TYPE_CHECKING:
    from .invoice import Invoice
    from .invoices_payments_invoice_payment_associated_payment import (
        InvoicesPaymentsInvoicePaymentAssociatedPayment,
    )


class InvoicePayment(pydantic.BaseModel):
    """
    The invoice payment object
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_paid: typing.Optional[int] = pydantic.Field(
        alias="amount_paid", default=None
    )
    """
    Amount that was actually paid for this invoice, in cents (or local equivalent). This field is null until the payment is `paid`. This amount can be less than the `amount_requested` if the PaymentIntent’s `amount_received` is not sufficient to pay all of the invoices that it is attached to.
    """
    amount_requested: int = pydantic.Field(
        alias="amount_requested",
    )
    """
    Amount intended to be paid toward this invoice, in cents (or local equivalent)
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
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    invoice: typing.Union[str, "Invoice", DeletedInvoice] = pydantic.Field(
        alias="invoice",
    )
    """
    The invoice that was paid.
    """
    is_default: bool = pydantic.Field(
        alias="is_default",
    )
    """
    Stripe automatically creates a default InvoicePayment when the invoice is finalized, and keeps it synchronized with the invoice’s `amount_remaining`. The PaymentIntent associated with the default payment can’t be edited or canceled directly.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["invoice_payment"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment: "InvoicesPaymentsInvoicePaymentAssociatedPayment" = pydantic.Field(
        alias="payment",
    )
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The status of the payment, one of `open`, `paid`, or `canceled`.
    """
    status_transitions: InvoicesPaymentsInvoicePaymentStatusTransitions = (
        pydantic.Field(
            alias="status_transitions",
        )
    )
