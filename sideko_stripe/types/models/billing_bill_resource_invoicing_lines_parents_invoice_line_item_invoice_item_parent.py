import pydantic
import typing

from .billing_bill_resource_invoicing_lines_common_proration_details import (
    BillingBillResourceInvoicingLinesCommonProrationDetails,
)


class BillingBillResourceInvoicingLinesParentsInvoiceLineItemInvoiceItemParent(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    invoice_item: str = pydantic.Field(
        alias="invoice_item",
    )
    """
    The invoice item that generated this line item
    """
    proration: bool = pydantic.Field(
        alias="proration",
    )
    """
    Whether this is a proration
    """
    proration_details: typing.Optional[
        BillingBillResourceInvoicingLinesCommonProrationDetails
    ] = pydantic.Field(alias="proration_details", default=None)
    subscription: typing.Optional[str] = pydantic.Field(
        alias="subscription", default=None
    )
    """
    The subscription that the invoice item belongs to
    """
