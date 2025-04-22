import pydantic


class InvoiceLineItemPeriod(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    end: int = pydantic.Field(
        alias="end",
    )
    """
    The end of the period, which must be greater than or equal to the start. This value is inclusive.
    """
    start: int = pydantic.Field(
        alias="start",
    )
    """
    The start of the period. This value is inclusive.
    """
