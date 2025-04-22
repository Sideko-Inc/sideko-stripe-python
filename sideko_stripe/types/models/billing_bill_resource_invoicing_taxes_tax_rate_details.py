import pydantic


class BillingBillResourceInvoicingTaxesTaxRateDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tax_rate: str = pydantic.Field(
        alias="tax_rate",
    )
