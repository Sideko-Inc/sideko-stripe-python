import pydantic


class BillingBillResourceInvoicingParentsInvoiceQuoteParent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    quote: str = pydantic.Field(
        alias="quote",
    )
    """
    The quote that generated this invoice
    """
