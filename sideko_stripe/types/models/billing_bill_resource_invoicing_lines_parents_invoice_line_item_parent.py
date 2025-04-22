import pydantic
import typing
import typing_extensions

from .billing_bill_resource_invoicing_lines_parents_invoice_line_item_invoice_item_parent import (
    BillingBillResourceInvoicingLinesParentsInvoiceLineItemInvoiceItemParent,
)
from .billing_bill_resource_invoicing_lines_parents_invoice_line_item_subscription_item_parent import (
    BillingBillResourceInvoicingLinesParentsInvoiceLineItemSubscriptionItemParent,
)


class BillingBillResourceInvoicingLinesParentsInvoiceLineItemParent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    invoice_item_details: typing.Optional[
        BillingBillResourceInvoicingLinesParentsInvoiceLineItemInvoiceItemParent
    ] = pydantic.Field(alias="invoice_item_details", default=None)
    subscription_item_details: typing.Optional[
        BillingBillResourceInvoicingLinesParentsInvoiceLineItemSubscriptionItemParent
    ] = pydantic.Field(alias="subscription_item_details", default=None)
    type_: typing_extensions.Literal[
        "invoice_item_details", "subscription_item_details"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of parent that generated this line item
    """
