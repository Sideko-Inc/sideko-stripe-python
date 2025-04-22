import pydantic
import typing
import typing_extensions

from .customer_balance_transaction_metadata import CustomerBalanceTransactionMetadata

if typing_extensions.TYPE_CHECKING:
    from .checkout_session import CheckoutSession
    from .credit_note import CreditNote
    from .customer import Customer
    from .invoice import Invoice


class CustomerBalanceTransaction(pydantic.BaseModel):
    """
    Each customer has a [Balance](https://stripe.com/docs/api/customers/object#customer_object-balance) value,
    which denotes a debit or credit that's automatically applied to their next invoice upon finalization.
    You may modify the value directly by using the [update customer API](https://stripe.com/docs/api/customers/update),
    or by creating a Customer Balance Transaction, which increments or decrements the customer's `balance` by the specified `amount`.

    Related guide: [Customer balance](https://stripe.com/docs/billing/customer/balance)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount of the transaction. A negative value is a credit for the customer's balance, and a positive value is a debit to the customer's `balance`.
    """
    checkout_session: typing.Optional[typing.Union[str, "CheckoutSession"]] = (
        pydantic.Field(alias="checkout_session", default=None)
    )
    """
    The ID of the checkout session (if any) that created the transaction.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    credit_note: typing.Optional[typing.Union[str, "CreditNote"]] = pydantic.Field(
        alias="credit_note", default=None
    )
    """
    The ID of the credit note (if any) related to the transaction.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: typing.Union[str, "Customer"] = pydantic.Field(
        alias="customer",
    )
    """
    The ID of the customer the transaction belongs to.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    ending_balance: int = pydantic.Field(
        alias="ending_balance",
    )
    """
    The customer's `balance` after the transaction was applied. A negative value decreases the amount due on the customer's next invoice. A positive value increases the amount due on the customer's next invoice.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    invoice: typing.Optional[typing.Union[str, "Invoice"]] = pydantic.Field(
        alias="invoice", default=None
    )
    """
    The ID of the invoice (if any) related to the transaction.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[CustomerBalanceTransactionMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["customer_balance_transaction"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    type_: typing_extensions.Literal[
        "adjustment",
        "applied_to_invoice",
        "checkout_session_subscription_payment",
        "checkout_session_subscription_payment_canceled",
        "credit_note",
        "initial",
        "invoice_overpaid",
        "invoice_too_large",
        "invoice_too_small",
        "migration",
        "unapplied_from_invoice",
        "unspent_receiver_credit",
    ] = pydantic.Field(
        alias="type",
    )
    """
    Transaction type: `adjustment`, `applied_to_invoice`, `credit_note`, `initial`, `invoice_overpaid`, `invoice_too_large`, `invoice_too_small`, `unspent_receiver_credit`, `unapplied_from_invoice`, `checkout_session_subscription_payment`, or `checkout_session_subscription_payment_canceled`. See the [Customer Balance page](https://stripe.com/docs/billing/customer/balance#types) to learn more about transaction types.
    """
