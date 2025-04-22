import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoicing_lines_parents_invoice_line_item_parent import (
    BillingBillResourceInvoicingLinesParentsInvoiceLineItemParent,
)
from .billing_bill_resource_invoicing_pricing_pricing import (
    BillingBillResourceInvoicingPricingPricing,
)
from .billing_bill_resource_invoicing_taxes_tax import (
    BillingBillResourceInvoicingTaxesTax,
)
from .invoice_line_item_period import InvoiceLineItemPeriod
from .line_item_metadata import LineItemMetadata

if typing_extensions.TYPE_CHECKING:
    from .discount import Discount
    from .discounts_resource_discount_amount import DiscountsResourceDiscountAmount
    from .invoices_resource_pretax_credit_amount import (
        InvoicesResourcePretaxCreditAmount,
    )
    from .subscription import Subscription


class LineItem(pydantic.BaseModel):
    """
    Invoice Line Items represent the individual lines within an [invoice](https://stripe.com/docs/api/invoices) and only exist within the context of an invoice.

    Each line item is backed by either an [invoice item](https://stripe.com/docs/api/invoiceitems) or a [subscription item](https://stripe.com/docs/api/subscription_items).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount, in cents (or local equivalent).
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
    discount_amounts: typing.Optional[
        typing.List["DiscountsResourceDiscountAmount"]
    ] = pydantic.Field(alias="discount_amounts", default=None)
    """
    The amount of discount calculated per discount for this line item.
    """
    discountable: bool = pydantic.Field(
        alias="discountable",
    )
    """
    If true, discounts will apply to this line item. Always false for prorations.
    """
    discounts: typing.List[typing.Union[str, "Discount"]] = pydantic.Field(
        alias="discounts",
    )
    """
    The discounts applied to the invoice line item. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    invoice: typing.Optional[str] = pydantic.Field(alias="invoice", default=None)
    """
    The ID of the invoice that contains this line item.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: LineItemMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Note that for line items with `type=subscription`, `metadata` reflects the current metadata from the subscription associated with the line item, unless the invoice line was directly updated with different metadata after creation.
    """
    object: typing_extensions.Literal["line_item"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    parent: typing.Optional[
        BillingBillResourceInvoicingLinesParentsInvoiceLineItemParent
    ] = pydantic.Field(alias="parent", default=None)
    period: InvoiceLineItemPeriod = pydantic.Field(
        alias="period",
    )
    pretax_credit_amounts: typing.Optional[
        typing.List["InvoicesResourcePretaxCreditAmount"]
    ] = pydantic.Field(alias="pretax_credit_amounts", default=None)
    """
    Contains pretax credit amounts (ex: discount, credit grants, etc) that apply to this line item.
    """
    pricing: typing.Optional[BillingBillResourceInvoicingPricingPricing] = (
        pydantic.Field(alias="pricing", default=None)
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    """
    The quantity of the subscription, if the line item is a subscription or a proration.
    """
    subscription: typing.Optional[typing.Union[str, "Subscription"]] = pydantic.Field(
        alias="subscription", default=None
    )
    taxes: typing.Optional[typing.List[BillingBillResourceInvoicingTaxesTax]] = (
        pydantic.Field(alias="taxes", default=None)
    )
    """
    The tax information of the line item.
    """
