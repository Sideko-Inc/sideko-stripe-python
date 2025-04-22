import pydantic
import typing


class BillingBillResourceInvoicingLinesCommonCreditedItems(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    invoice: str = pydantic.Field(
        alias="invoice",
    )
    """
    Invoice containing the credited invoice line items
    """
    invoice_line_items: typing.List[str] = pydantic.Field(
        alias="invoice_line_items",
    )
    """
    Credited invoice line items
    """
