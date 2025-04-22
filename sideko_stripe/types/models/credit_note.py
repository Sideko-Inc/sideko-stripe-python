import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoicing_taxes_tax import (
    BillingBillResourceInvoicingTaxesTax,
)
from .credit_note_metadata import CreditNoteMetadata
from .deleted_customer import DeletedCustomer
from .invoices_resource_shipping_cost import InvoicesResourceShippingCost

if typing_extensions.TYPE_CHECKING:
    from .credit_note_lines import CreditNoteLines
    from .credit_note_refund import CreditNoteRefund
    from .credit_notes_pretax_credit_amount import CreditNotesPretaxCreditAmount
    from .customer import Customer
    from .customer_balance_transaction import CustomerBalanceTransaction
    from .discounts_resource_discount_amount import DiscountsResourceDiscountAmount
    from .invoice import Invoice


class CreditNote(pydantic.BaseModel):
    """
    Issue a credit note to adjust an invoice's amount after the invoice is finalized.

    Related guide: [Credit notes](https://stripe.com/docs/billing/invoices/credit-notes)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The integer amount in cents (or local equivalent) representing the total amount of the credit note, including tax.
    """
    amount_shipping: int = pydantic.Field(
        alias="amount_shipping",
    )
    """
    This is the sum of all the shipping amounts.
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
    customer: typing.Union[str, "Customer", DeletedCustomer] = pydantic.Field(
        alias="customer",
    )
    """
    ID of the customer.
    """
    customer_balance_transaction: typing.Optional[
        typing.Union[str, "CustomerBalanceTransaction"]
    ] = pydantic.Field(alias="customer_balance_transaction", default=None)
    """
    Customer balance transaction related to this credit note.
    """
    discount_amount: int = pydantic.Field(
        alias="discount_amount",
    )
    """
    The integer amount in cents (or local equivalent) representing the total amount of discount that was credited.
    """
    discount_amounts: typing.List["DiscountsResourceDiscountAmount"] = pydantic.Field(
        alias="discount_amounts",
    )
    """
    The aggregate amounts calculated per discount for all line items.
    """
    effective_at: typing.Optional[int] = pydantic.Field(
        alias="effective_at", default=None
    )
    """
    The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    invoice: typing.Union[str, "Invoice"] = pydantic.Field(
        alias="invoice",
    )
    """
    ID of the invoice.
    """
    lines: "CreditNoteLines" = pydantic.Field(
        alias="lines",
    )
    """
    Line items that make up the credit note
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    memo: typing.Optional[str] = pydantic.Field(alias="memo", default=None)
    """
    Customer-facing text that appears on the credit note PDF.
    """
    metadata: typing.Optional[CreditNoteMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    number: str = pydantic.Field(
        alias="number",
    )
    """
    A unique number that identifies this particular credit note and appears on the PDF of the credit note and its associated invoice.
    """
    object: typing_extensions.Literal["credit_note"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    out_of_band_amount: typing.Optional[int] = pydantic.Field(
        alias="out_of_band_amount", default=None
    )
    """
    Amount that was credited outside of Stripe.
    """
    pdf: str = pydantic.Field(
        alias="pdf",
    )
    """
    The link to download the PDF of the credit note.
    """
    pretax_credit_amounts: typing.List["CreditNotesPretaxCreditAmount"] = (
        pydantic.Field(
            alias="pretax_credit_amounts",
        )
    )
    """
    The pretax credit amounts (ex: discount, credit grants, etc) for all line items.
    """
    reason: typing.Optional[
        typing_extensions.Literal[
            "duplicate", "fraudulent", "order_change", "product_unsatisfactory"
        ]
    ] = pydantic.Field(alias="reason", default=None)
    """
    Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
    """
    refunds: typing.List["CreditNoteRefund"] = pydantic.Field(
        alias="refunds",
    )
    """
    Refunds related to this credit note.
    """
    shipping_cost: typing.Optional[InvoicesResourceShippingCost] = pydantic.Field(
        alias="shipping_cost", default=None
    )
    status: typing_extensions.Literal["issued", "void"] = pydantic.Field(
        alias="status",
    )
    """
    Status of this credit note, one of `issued` or `void`. Learn more about [voiding credit notes](https://stripe.com/docs/billing/invoices/credit-notes#voiding).
    """
    subtotal: int = pydantic.Field(
        alias="subtotal",
    )
    """
    The integer amount in cents (or local equivalent) representing the amount of the credit note, excluding exclusive tax and invoice level discounts.
    """
    subtotal_excluding_tax: typing.Optional[int] = pydantic.Field(
        alias="subtotal_excluding_tax", default=None
    )
    """
    The integer amount in cents (or local equivalent) representing the amount of the credit note, excluding all tax and invoice level discounts.
    """
    total: int = pydantic.Field(
        alias="total",
    )
    """
    The integer amount in cents (or local equivalent) representing the total amount of the credit note, including tax and all discount.
    """
    total_excluding_tax: typing.Optional[int] = pydantic.Field(
        alias="total_excluding_tax", default=None
    )
    """
    The integer amount in cents (or local equivalent) representing the total amount of the credit note, excluding tax, but including discounts.
    """
    total_taxes: typing.Optional[typing.List[BillingBillResourceInvoicingTaxesTax]] = (
        pydantic.Field(alias="total_taxes", default=None)
    )
    """
    The aggregate tax information for all line items.
    """
    type_: typing_extensions.Literal["post_payment", "pre_payment"] = pydantic.Field(
        alias="type",
    )
    """
    Type of this credit note, one of `pre_payment` or `post_payment`. A `pre_payment` credit note means it was issued when the invoice was open. A `post_payment` credit note means it was issued when the invoice was paid.
    """
    voided_at: typing.Optional[int] = pydantic.Field(alias="voided_at", default=None)
    """
    The time that the credit note was voided.
    """
