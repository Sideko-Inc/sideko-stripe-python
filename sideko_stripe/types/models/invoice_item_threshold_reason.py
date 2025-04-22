import pydantic
import typing


class InvoiceItemThresholdReason(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    line_item_ids: typing.List[str] = pydantic.Field(
        alias="line_item_ids",
    )
    """
    The IDs of the line items that triggered the threshold invoice.
    """
    usage_gte: int = pydantic.Field(
        alias="usage_gte",
    )
    """
    The quantity threshold boundary that applied to the given line item.
    """
