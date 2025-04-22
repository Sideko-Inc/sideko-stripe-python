import pydantic


class BillingBillResourceInvoicingPricingPricingPriceDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    price: str = pydantic.Field(
        alias="price",
    )
    """
    The ID of the price this item is associated with.
    """
    product: str = pydantic.Field(
        alias="product",
    )
    """
    The ID of the product this item is associated with.
    """
