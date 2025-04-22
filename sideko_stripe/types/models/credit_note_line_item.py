import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoicing_taxes_tax import (
    BillingBillResourceInvoicingTaxesTax,
)
from .tax_rate import TaxRate

if typing_extensions.TYPE_CHECKING:
    from .credit_notes_pretax_credit_amount import CreditNotesPretaxCreditAmount
    from .discounts_resource_discount_amount import DiscountsResourceDiscountAmount


class CreditNoteLineItem(pydantic.BaseModel):
    """
    The credit note line item object
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The integer amount in cents (or local equivalent) representing the gross amount being credited for this line item, excluding (exclusive) tax and discounts.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    Description of the item being credited.
    """
    discount_amount: int = pydantic.Field(
        alias="discount_amount",
    )
    """
    The integer amount in cents (or local equivalent) representing the discount being credited for this line item.
    """
    discount_amounts: typing.List["DiscountsResourceDiscountAmount"] = pydantic.Field(
        alias="discount_amounts",
    )
    """
    The amount of discount calculated per discount for this line item
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    invoice_line_item: typing.Optional[str] = pydantic.Field(
        alias="invoice_line_item", default=None
    )
    """
    ID of the invoice line item being credited
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["credit_note_line_item"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    pretax_credit_amounts: typing.List["CreditNotesPretaxCreditAmount"] = (
        pydantic.Field(
            alias="pretax_credit_amounts",
        )
    )
    """
    The pretax credit amounts (ex: discount, credit grants, etc) for this line item.
    """
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    """
    The number of units of product being credited.
    """
    tax_rates: typing.List[TaxRate] = pydantic.Field(
        alias="tax_rates",
    )
    """
    The tax rates which apply to the line item.
    """
    taxes: typing.Optional[typing.List[BillingBillResourceInvoicingTaxesTax]] = (
        pydantic.Field(alias="taxes", default=None)
    )
    """
    The tax information of the line item.
    """
    type_: typing_extensions.Literal["custom_line_item", "invoice_line_item"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    The type of the credit note line item, one of `invoice_line_item` or `custom_line_item`. When the type is `invoice_line_item` there is an additional `invoice_line_item` property on the resource the value of which is the id of the credited line item on the invoice.
    """
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    """
    The cost of each unit of product being credited.
    """
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
    """
    Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.
    """
