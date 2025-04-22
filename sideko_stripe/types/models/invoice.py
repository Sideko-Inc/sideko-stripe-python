import pydantic
import typing
import typing_extensions

from .address import Address
from .application import Application
from .billing_bill_resource_invoicing_taxes_tax import (
    BillingBillResourceInvoicingTaxesTax,
)
from .deleted_application import DeletedApplication
from .deleted_customer import DeletedCustomer
from .deleted_tax_id import DeletedTaxId
from .invoice_metadata import InvoiceMetadata
from .invoice_setting_custom_field import InvoiceSettingCustomField
from .invoice_threshold_reason import InvoiceThresholdReason
from .invoices_payment_settings import InvoicesPaymentSettings
from .invoices_resource_confirmation_secret import InvoicesResourceConfirmationSecret
from .invoices_resource_invoice_rendering import InvoicesResourceInvoiceRendering
from .invoices_resource_invoice_tax_id import InvoicesResourceInvoiceTaxId
from .invoices_resource_shipping_cost import InvoicesResourceShippingCost
from .invoices_resource_status_transitions import InvoicesResourceStatusTransitions
from .shipping import Shipping
from .source import Source
from .tax_rate import TaxRate
from .test_helpers_test_clock import TestHelpersTestClock

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .api_errors import ApiErrors
    from .automatic_tax import AutomaticTax
    from .bank_account import BankAccount
    from .billing_bill_resource_invoicing_parents_invoice_parent import (
        BillingBillResourceInvoicingParentsInvoiceParent,
    )
    from .card import Card
    from .connect_account_reference import ConnectAccountReference
    from .customer import Customer
    from .deleted_discount import DeletedDiscount
    from .discount import Discount
    from .discounts_resource_discount_amount import DiscountsResourceDiscountAmount
    from .invoice_lines import InvoiceLines
    from .invoice_payments import InvoicePayments
    from .invoices_resource_from_invoice import InvoicesResourceFromInvoice
    from .invoices_resource_pretax_credit_amount import (
        InvoicesResourcePretaxCreditAmount,
    )
    from .payment_method import PaymentMethod
    from .tax_id import TaxId


class Invoice(pydantic.BaseModel):
    """
    Invoices are statements of amounts owed by a customer, and are either
    generated one-off, or generated periodically from a subscription.

    They contain [invoice items](https://stripe.com/docs/api#invoiceitems), and proration adjustments
    that may be caused by subscription upgrades/downgrades (if necessary).

    If your invoice is configured to be billed through automatic charges,
    Stripe automatically finalizes your invoice and attempts payment. Note
    that finalizing the invoice,
    [when automatic](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection), does
    not happen immediately as the invoice is created. Stripe waits
    until one hour after the last webhook was successfully sent (or the last
    webhook timed out after failing). If you (and the platforms you may have
    connected to) have no webhooks configured, Stripe waits one hour after
    creation to finalize the invoice.

    If your invoice is configured to be billed by sending an email, then based on your
    [email settings](https://dashboard.stripe.com/account/billing/automatic),
    Stripe will email the invoice to your customer and await payment. These
    emails can contain a link to a hosted page to pay the invoice.

    Stripe applies any customer credit on the account before determining the
    amount due for the invoice (i.e., the amount that will be actually
    charged). If the amount due for the invoice is less than Stripe's [minimum allowed charge
    per currency](/docs/currencies#minimum-and-maximum-charge-amounts), the
    invoice is automatically marked paid, and we add the amount due to the
    customer's credit balance which is applied to the next invoice.

    More details on the customer's credit balance are
    [here](https://stripe.com/docs/billing/customer/balance).

    Related guide: [Send invoices to customers](https://stripe.com/docs/billing/invoices/sending)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_country: typing.Optional[str] = pydantic.Field(
        alias="account_country", default=None
    )
    """
    The country of the business associated with this invoice, most often the business creating the invoice.
    """
    account_name: typing.Optional[str] = pydantic.Field(
        alias="account_name", default=None
    )
    """
    The public name of the business associated with this invoice, most often the business creating the invoice.
    """
    account_tax_ids: typing.Optional[
        typing.List[typing.Union[str, "TaxId", DeletedTaxId]]
    ] = pydantic.Field(alias="account_tax_ids", default=None)
    """
    The account tax IDs associated with the invoice. Only editable when the invoice is a draft.
    """
    amount_due: int = pydantic.Field(
        alias="amount_due",
    )
    """
    Final amount due at this time for this invoice. If the invoice's total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the `amount_due` may be 0. If there is a positive `starting_balance` for the invoice (the customer owes money), the `amount_due` will also take that into account. The charge that gets generated for the invoice will be for the amount specified in `amount_due`.
    """
    amount_overpaid: int = pydantic.Field(
        alias="amount_overpaid",
    )
    """
    Amount that was overpaid on the invoice. The amount overpaid is credited to the customer's credit balance.
    """
    amount_paid: int = pydantic.Field(
        alias="amount_paid",
    )
    """
    The amount, in cents (or local equivalent), that was paid.
    """
    amount_remaining: int = pydantic.Field(
        alias="amount_remaining",
    )
    """
    The difference between amount_due and amount_paid, in cents (or local equivalent).
    """
    amount_shipping: int = pydantic.Field(
        alias="amount_shipping",
    )
    """
    This is the sum of all the shipping amounts.
    """
    application: typing.Optional[typing.Union[str, Application, DeletedApplication]] = (
        pydantic.Field(alias="application", default=None)
    )
    """
    ID of the Connect Application that created the invoice.
    """
    attempt_count: int = pydantic.Field(
        alias="attempt_count",
    )
    """
    Number of payment attempts made for this invoice, from the perspective of the payment retry schedule. Any payment attempt counts as the first attempt, and subsequently only automatic retries increment the attempt count. In other words, manual payment attempts after the first attempt do not affect the retry schedule. If a failure is returned with a non-retryable return code, the invoice can no longer be retried unless a new payment method is obtained. Retries will continue to be scheduled, and attempt_count will continue to increment, but retries will only be executed if a new payment method is obtained.
    """
    attempted: bool = pydantic.Field(
        alias="attempted",
    )
    """
    Whether an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the `invoice.created` webhook, for example, so you might not want to display that invoice as unpaid to your users.
    """
    auto_advance: bool = pydantic.Field(
        alias="auto_advance",
    )
    """
    Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action.
    """
    automatic_tax: "AutomaticTax" = pydantic.Field(
        alias="automatic_tax",
    )
    automatically_finalizes_at: typing.Optional[int] = pydantic.Field(
        alias="automatically_finalizes_at", default=None
    )
    """
    The time when this invoice is currently scheduled to be automatically finalized. The field will be `null` if the invoice is not scheduled to finalize in the future. If the invoice is not in the draft state, this field will always be `null` - see `finalized_at` for the time when an already-finalized invoice was finalized.
    """
    billing_reason: typing.Optional[
        typing_extensions.Literal[
            "automatic_pending_invoice_item_invoice",
            "manual",
            "quote_accept",
            "subscription",
            "subscription_create",
            "subscription_cycle",
            "subscription_threshold",
            "subscription_update",
            "upcoming",
        ]
    ] = pydantic.Field(alias="billing_reason", default=None)
    """
    Indicates the reason why the invoice was created.
    
    * `manual`: Unrelated to a subscription, for example, created via the invoice editor.
    * `subscription`: No longer in use. Applies to subscriptions from before May 2018 where no distinction was made between updates, cycles, and thresholds.
    * `subscription_create`: A new subscription was created.
    * `subscription_cycle`: A subscription advanced into a new period.
    * `subscription_threshold`: A subscription reached a billing threshold.
    * `subscription_update`: A subscription was updated.
    * `upcoming`: Reserved for simulated invoices, per the upcoming invoice endpoint.
    """
    collection_method: typing_extensions.Literal[
        "charge_automatically", "send_invoice"
    ] = pydantic.Field(
        alias="collection_method",
    )
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions.
    """
    confirmation_secret: typing.Optional[InvoicesResourceConfirmationSecret] = (
        pydantic.Field(alias="confirmation_secret", default=None)
    )
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
    custom_fields: typing.Optional[typing.List[InvoiceSettingCustomField]] = (
        pydantic.Field(alias="custom_fields", default=None)
    )
    """
    Custom fields displayed on the invoice.
    """
    customer: typing.Union[str, "Customer", DeletedCustomer] = pydantic.Field(
        alias="customer",
    )
    """
    The ID of the customer who will be billed.
    """
    customer_address: typing.Optional[Address] = pydantic.Field(
        alias="customer_address", default=None
    )
    customer_email: typing.Optional[str] = pydantic.Field(
        alias="customer_email", default=None
    )
    """
    The customer's email. Until the invoice is finalized, this field will equal `customer.email`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_name: typing.Optional[str] = pydantic.Field(
        alias="customer_name", default=None
    )
    """
    The customer's name. Until the invoice is finalized, this field will equal `customer.name`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_phone: typing.Optional[str] = pydantic.Field(
        alias="customer_phone", default=None
    )
    """
    The customer's phone number. Until the invoice is finalized, this field will equal `customer.phone`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_shipping: typing.Optional[Shipping] = pydantic.Field(
        alias="customer_shipping", default=None
    )
    customer_tax_exempt: typing.Optional[
        typing_extensions.Literal["exempt", "none", "reverse"]
    ] = pydantic.Field(alias="customer_tax_exempt", default=None)
    """
    The customer's tax exempt status. Until the invoice is finalized, this field will equal `customer.tax_exempt`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_tax_ids: typing.Optional[typing.List[InvoicesResourceInvoiceTaxId]] = (
        pydantic.Field(alias="customer_tax_ids", default=None)
    )
    """
    The customer's tax IDs. Until the invoice is finalized, this field will contain the same tax IDs as `customer.tax_ids`. Once the invoice is finalized, this field will no longer be updated.
    """
    default_payment_method: typing.Optional[typing.Union[str, "PaymentMethod"]] = (
        pydantic.Field(alias="default_payment_method", default=None)
    )
    """
    ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings.
    """
    default_source: typing.Optional[
        typing.Union[str, "BankAccount", "Card", Source]
    ] = pydantic.Field(alias="default_source", default=None)
    """
    ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source.
    """
    default_tax_rates: typing.List[TaxRate] = pydantic.Field(
        alias="default_tax_rates",
    )
    """
    The tax rates applied to this invoice, if any.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard.
    """
    discounts: typing.List[typing.Union[str, "Discount", "DeletedDiscount"]] = (
        pydantic.Field(
            alias="discounts",
        )
    )
    """
    The discounts applied to the invoice. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.
    """
    due_date: typing.Optional[int] = pydantic.Field(alias="due_date", default=None)
    """
    The date on which payment for this invoice is due. This value will be `null` for invoices where `collection_method=charge_automatically`.
    """
    effective_at: typing.Optional[int] = pydantic.Field(
        alias="effective_at", default=None
    )
    """
    The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt.
    """
    ending_balance: typing.Optional[int] = pydantic.Field(
        alias="ending_balance", default=None
    )
    """
    Ending customer balance after the invoice is finalized. Invoices are finalized approximately an hour after successful webhook delivery or when payment collection is attempted for the invoice. If the invoice has not been finalized yet, this will be null.
    """
    footer: typing.Optional[str] = pydantic.Field(alias="footer", default=None)
    """
    Footer displayed on the invoice.
    """
    from_invoice: typing.Optional["InvoicesResourceFromInvoice"] = pydantic.Field(
        alias="from_invoice", default=None
    )
    hosted_invoice_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_invoice_url", default=None
    )
    """
    The URL for the hosted invoice page, which allows customers to view and pay an invoice. If the invoice has not been finalized yet, this will be null.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object. This property is always present unless the invoice is an upcoming invoice. See [Retrieve an upcoming invoice](https://stripe.com/docs/api/invoices/upcoming) for more details.
    """
    invoice_pdf: typing.Optional[str] = pydantic.Field(
        alias="invoice_pdf", default=None
    )
    """
    The link to download the PDF for the invoice. If the invoice has not been finalized yet, this will be null.
    """
    issuer: "ConnectAccountReference" = pydantic.Field(
        alias="issuer",
    )
    last_finalization_error: typing.Optional["ApiErrors"] = pydantic.Field(
        alias="last_finalization_error", default=None
    )
    latest_revision: typing.Optional[typing.Union[str, "Invoice"]] = pydantic.Field(
        alias="latest_revision", default=None
    )
    """
    The ID of the most recent non-draft revision of this invoice
    """
    lines: "InvoiceLines" = pydantic.Field(
        alias="lines",
    )
    """
    The individual line items that make up the invoice. `lines` is sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[InvoiceMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_payment_attempt: typing.Optional[int] = pydantic.Field(
        alias="next_payment_attempt", default=None
    )
    """
    The time at which payment will next be attempted. This value will be `null` for invoices where `collection_method=send_invoice`.
    """
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    """
    A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer's unique invoice_prefix if it is specified.
    """
    object: typing_extensions.Literal["invoice"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details.
    """
    parent: typing.Optional["BillingBillResourceInvoicingParentsInvoiceParent"] = (
        pydantic.Field(alias="parent", default=None)
    )
    payment_settings: InvoicesPaymentSettings = pydantic.Field(
        alias="payment_settings",
    )
    payments: typing.Optional["InvoicePayments"] = pydantic.Field(
        alias="payments", default=None
    )
    """
    Payments for this invoice
    """
    period_end: int = pydantic.Field(
        alias="period_end",
    )
    """
    End of the usage period during which invoice items were added to this invoice. This looks back one period for a subscription invoice. Use the [line item period](/api/invoices/line_item#invoice_line_item_object-period) to get the service period for each price.
    """
    period_start: int = pydantic.Field(
        alias="period_start",
    )
    """
    Start of the usage period during which invoice items were added to this invoice. This looks back one period for a subscription invoice. Use the [line item period](/api/invoices/line_item#invoice_line_item_object-period) to get the service period for each price.
    """
    post_payment_credit_notes_amount: int = pydantic.Field(
        alias="post_payment_credit_notes_amount",
    )
    """
    Total amount of all post-payment credit notes issued for this invoice.
    """
    pre_payment_credit_notes_amount: int = pydantic.Field(
        alias="pre_payment_credit_notes_amount",
    )
    """
    Total amount of all pre-payment credit notes issued for this invoice.
    """
    receipt_number: typing.Optional[str] = pydantic.Field(
        alias="receipt_number", default=None
    )
    """
    This is the transaction number that appears on email receipts sent for this invoice.
    """
    rendering: typing.Optional[InvoicesResourceInvoiceRendering] = pydantic.Field(
        alias="rendering", default=None
    )
    shipping_cost: typing.Optional[InvoicesResourceShippingCost] = pydantic.Field(
        alias="shipping_cost", default=None
    )
    shipping_details: typing.Optional[Shipping] = pydantic.Field(
        alias="shipping_details", default=None
    )
    starting_balance: int = pydantic.Field(
        alias="starting_balance",
    )
    """
    Starting customer balance before the invoice is finalized. If the invoice has not been finalized yet, this will be the current customer balance. For revision invoices, this also includes any customer balance that was applied to the original invoice.
    """
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    """
    Extra information about an invoice for the customer's credit card statement.
    """
    status: typing.Optional[
        typing_extensions.Literal["draft", "open", "paid", "uncollectible", "void"]
    ] = pydantic.Field(alias="status", default=None)
    """
    The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview)
    """
    status_transitions: InvoicesResourceStatusTransitions = pydantic.Field(
        alias="status_transitions",
    )
    subtotal: int = pydantic.Field(
        alias="subtotal",
    )
    """
    Total of all subscriptions, invoice items, and prorations on the invoice before any invoice level discount or exclusive tax is applied. Item discounts are already incorporated
    """
    subtotal_excluding_tax: typing.Optional[int] = pydantic.Field(
        alias="subtotal_excluding_tax", default=None
    )
    """
    The integer amount in cents (or local equivalent) representing the subtotal of the invoice before any invoice level discount or tax is applied. Item discounts are already incorporated
    """
    test_clock: typing.Optional[typing.Union[str, TestHelpersTestClock]] = (
        pydantic.Field(alias="test_clock", default=None)
    )
    """
    ID of the test clock this invoice belongs to.
    """
    threshold_reason: typing.Optional[InvoiceThresholdReason] = pydantic.Field(
        alias="threshold_reason", default=None
    )
    total: int = pydantic.Field(
        alias="total",
    )
    """
    Total after discounts and taxes.
    """
    total_discount_amounts: typing.Optional[
        typing.List["DiscountsResourceDiscountAmount"]
    ] = pydantic.Field(alias="total_discount_amounts", default=None)
    """
    The aggregate amounts calculated per discount across all line items.
    """
    total_excluding_tax: typing.Optional[int] = pydantic.Field(
        alias="total_excluding_tax", default=None
    )
    """
    The integer amount in cents (or local equivalent) representing the total amount of the invoice including all discounts but excluding all tax.
    """
    total_pretax_credit_amounts: typing.Optional[
        typing.List["InvoicesResourcePretaxCreditAmount"]
    ] = pydantic.Field(alias="total_pretax_credit_amounts", default=None)
    """
    Contains pretax credit amounts (ex: discount, credit grants, etc) that apply to this invoice. This is a combined list of total_pretax_credit_amounts across all invoice line items.
    """
    total_taxes: typing.Optional[typing.List[BillingBillResourceInvoicingTaxesTax]] = (
        pydantic.Field(alias="total_taxes", default=None)
    )
    """
    The aggregate tax information of all line items.
    """
    webhooks_delivered_at: typing.Optional[int] = pydantic.Field(
        alias="webhooks_delivered_at", default=None
    )
    """
    Invoices are automatically paid or sent 1 hour after webhooks are delivered, or until all webhook delivery attempts have [been exhausted](https://stripe.com/docs/billing/webhooks#understand). This field tracks the time when webhooks for this invoice were successfully delivered. If the invoice had no webhooks to deliver, this will be set while the invoice is being created.
    """
