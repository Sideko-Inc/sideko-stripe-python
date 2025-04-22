import pydantic
import typing

from .invoice_item_threshold_reason import InvoiceItemThresholdReason


class InvoiceThresholdReason(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_gte: typing.Optional[int] = pydantic.Field(alias="amount_gte", default=None)
    """
    The total invoice amount threshold boundary if it triggered the threshold invoice.
    """
    item_reasons: typing.List[InvoiceItemThresholdReason] = pydantic.Field(
        alias="item_reasons",
    )
    """
    Indicates which line items triggered a threshold invoice.
    """
