import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoice_item_parents_invoice_item_parent import (
    BillingBillResourceInvoiceItemParentsInvoiceItemParent,
)
from .billing_bill_resource_invoicing_pricing_pricing import (
    BillingBillResourceInvoicingPricingPricing,
)
from .deleted_customer import DeletedCustomer
from .invoice_line_item_period import InvoiceLineItemPeriod
from .invoiceitem_metadata import InvoiceitemMetadata
from .tax_rate import TaxRate
from .test_helpers_test_clock import TestHelpersTestClock

if typing_extensions.TYPE_CHECKING:
    from .customer import Customer
    from .discount import Discount
    from .invoice import Invoice


class Invoiceitem(pydantic.BaseModel):
    """
    Invoice Items represent the component lines of an [invoice](https://stripe.com/docs/api/invoices). An invoice item is added to an
    invoice by creating or updating it with an `invoice` field, at which point it will be included as
    [an invoice line item](https://stripe.com/docs/api/invoices/line_item) within
    [invoice.lines](https://stripe.com/docs/api/invoices/object#invoice_object-lines).

    Invoice Items can be created before you are ready to actually send the invoice. This can be particularly useful when combined
    with a [subscription](https://stripe.com/docs/api/subscriptions). Sometimes you want to add a charge or credit to a customer, but actually charge
    or credit the customer’s card only at the end of a regular billing cycle. This is useful for combining several charges
    (to minimize per-transaction fees), or for having Stripe tabulate your usage-based billing totals.

    Related guides: [Integrate with the Invoicing API](https://stripe.com/docs/invoicing/integration), [Subscription Invoices](https://stripe.com/docs/billing/invoices/subscription#adding-upcoming-invoice-items).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount (in the `currency` specified) of the invoice item. This should always be equal to `unit_amount * quantity`.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: typing.Union[str, "Customer", DeletedCustomer] = pydantic.Field(
        alias="customer",
    )
    """
    The ID of the customer who will be billed when this invoice item is billed.
    """
    date: int = pydantic.Field(
        alias="date",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    discountable: bool = pydantic.Field(
        alias="discountable",
    )
    """
    If true, discounts will apply to this invoice item. Always false for prorations.
    """
    discounts: typing.Optional[typing.List[typing.Union[str, "Discount"]]] = (
        pydantic.Field(alias="discounts", default=None)
    )
    """
    The discounts which apply to the invoice item. Item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.
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
    The ID of the invoice this invoice item belongs to.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[InvoiceitemMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["invoiceitem"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    parent: typing.Optional[BillingBillResourceInvoiceItemParentsInvoiceItemParent] = (
        pydantic.Field(alias="parent", default=None)
    )
    period: InvoiceLineItemPeriod = pydantic.Field(
        alias="period",
    )
    pricing: typing.Optional[BillingBillResourceInvoicingPricingPricing] = (
        pydantic.Field(alias="pricing", default=None)
    )
    proration: bool = pydantic.Field(
        alias="proration",
    )
    """
    Whether the invoice item was created automatically as a proration adjustment when the customer switched plans.
    """
    quantity: int = pydantic.Field(
        alias="quantity",
    )
    """
    Quantity of units for the invoice item. If the invoice item is a proration, the quantity of the subscription that the proration was computed for.
    """
    tax_rates: typing.Optional[typing.List[TaxRate]] = pydantic.Field(
        alias="tax_rates", default=None
    )
    """
    The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item.
    """
    test_clock: typing.Optional[typing.Union[str, TestHelpersTestClock]] = (
        pydantic.Field(alias="test_clock", default=None)
    )
    """
    ID of the test clock this invoice item belongs to.
    """
