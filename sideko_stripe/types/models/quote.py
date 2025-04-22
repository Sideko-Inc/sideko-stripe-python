import pydantic
import typing
import typing_extensions

from .application import Application
from .deleted_application import DeletedApplication
from .deleted_customer import DeletedCustomer
from .deleted_invoice import DeletedInvoice
from .quote_metadata import QuoteMetadata
from .quotes_resource_status_transitions import QuotesResourceStatusTransitions
from .quotes_resource_subscription_data_subscription_data import (
    QuotesResourceSubscriptionDataSubscriptionData,
)
from .tax_rate import TaxRate
from .test_helpers_test_clock import TestHelpersTestClock

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .customer import Customer
    from .discount import Discount
    from .invoice import Invoice
    from .invoice_setting_quote_setting import InvoiceSettingQuoteSetting
    from .quote_line_items import QuoteLineItems
    from .quotes_resource_automatic_tax import QuotesResourceAutomaticTax
    from .quotes_resource_computed import QuotesResourceComputed
    from .quotes_resource_from_quote import QuotesResourceFromQuote
    from .quotes_resource_total_details import QuotesResourceTotalDetails
    from .quotes_resource_transfer_data import QuotesResourceTransferData
    from .subscription import Subscription
    from .subscription_schedule1 import SubscriptionSchedule1


class Quote(pydantic.BaseModel):
    """
    A Quote is a way to model prices that you'd like to provide to a customer.
    Once accepted, it will automatically create an invoice, subscription or subscription schedule.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_subtotal: int = pydantic.Field(
        alias="amount_subtotal",
    )
    """
    Total before any discounts or taxes are applied.
    """
    amount_total: int = pydantic.Field(
        alias="amount_total",
    )
    """
    Total after discounts and taxes are applied.
    """
    application: typing.Optional[typing.Union[str, Application, DeletedApplication]] = (
        pydantic.Field(alias="application", default=None)
    )
    """
    ID of the Connect Application that created the quote.
    """
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Only applicable if there are no line items with recurring prices on the quote.
    """
    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. Only applicable if there are line items with recurring prices on the quote.
    """
    automatic_tax: "QuotesResourceAutomaticTax" = pydantic.Field(
        alias="automatic_tax",
    )
    collection_method: typing_extensions.Literal[
        "charge_automatically", "send_invoice"
    ] = pydantic.Field(
        alias="collection_method",
    )
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or on finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    """
    computed: "QuotesResourceComputed" = pydantic.Field(
        alias="computed",
    )
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: typing.Optional[typing.Union[str, "Customer", DeletedCustomer]] = (
        pydantic.Field(alias="customer", default=None)
    )
    """
    The customer which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
    """
    default_tax_rates: typing.Optional[typing.List[typing.Union[str, TaxRate]]] = (
        pydantic.Field(alias="default_tax_rates", default=None)
    )
    """
    The tax rates applied to this quote.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    A description that will be displayed on the quote PDF.
    """
    discounts: typing.List[typing.Union[str, "Discount"]] = pydantic.Field(
        alias="discounts",
    )
    """
    The discounts applied to this quote.
    """
    expires_at: int = pydantic.Field(
        alias="expires_at",
    )
    """
    The date on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
    """
    footer: typing.Optional[str] = pydantic.Field(alias="footer", default=None)
    """
    A footer that will be displayed on the quote PDF.
    """
    from_quote: typing.Optional["QuotesResourceFromQuote"] = pydantic.Field(
        alias="from_quote", default=None
    )
    header: typing.Optional[str] = pydantic.Field(alias="header", default=None)
    """
    A header that will be displayed on the quote PDF.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    invoice: typing.Optional[typing.Union[str, "Invoice", DeletedInvoice]] = (
        pydantic.Field(alias="invoice", default=None)
    )
    """
    The invoice that was created from this quote.
    """
    invoice_settings: "InvoiceSettingQuoteSetting" = pydantic.Field(
        alias="invoice_settings",
    )
    line_items: typing.Optional["QuoteLineItems"] = pydantic.Field(
        alias="line_items", default=None
    )
    """
    A list of items the customer is being quoted for.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: QuoteMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    """
    A unique number that identifies this particular quote. This number is assigned once the quote is [finalized](https://stripe.com/docs/quotes/overview#finalize).
    """
    object: typing_extensions.Literal["quote"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details.
    """
    status: typing_extensions.Literal["accepted", "canceled", "draft", "open"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The status of the quote.
    """
    status_transitions: QuotesResourceStatusTransitions = pydantic.Field(
        alias="status_transitions",
    )
    subscription: typing.Optional[typing.Union[str, "Subscription"]] = pydantic.Field(
        alias="subscription", default=None
    )
    """
    The subscription that was created or updated from this quote.
    """
    subscription_data: QuotesResourceSubscriptionDataSubscriptionData = pydantic.Field(
        alias="subscription_data",
    )
    subscription_schedule: typing.Optional[
        typing.Union[str, "SubscriptionSchedule1"]
    ] = pydantic.Field(alias="subscription_schedule", default=None)
    """
    The subscription schedule that was created or updated from this quote.
    """
    test_clock: typing.Optional[typing.Union[str, TestHelpersTestClock]] = (
        pydantic.Field(alias="test_clock", default=None)
    )
    """
    ID of the test clock this quote belongs to.
    """
    total_details: "QuotesResourceTotalDetails" = pydantic.Field(
        alias="total_details",
    )
    transfer_data: typing.Optional["QuotesResourceTransferData"] = pydantic.Field(
        alias="transfer_data", default=None
    )
