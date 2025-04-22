import pydantic


class TaxProductResourceTaxTransactionLineItemResourceReversal(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    original_line_item: str = pydantic.Field(
        alias="original_line_item",
    )
    """
    The `id` of the line item to reverse in the original transaction.
    """
