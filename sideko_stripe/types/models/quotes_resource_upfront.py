import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .quotes_resource_total_details import QuotesResourceTotalDetails
    from .quotes_resource_upfront_line_items import QuotesResourceUpfrontLineItems


class QuotesResourceUpfront(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_subtotal: int = pydantic.Field(
        alias="amount_subtotal",
    )
    """
    Total before any discounts or taxes are applied.
    """
    amount_total: int = pydantic.Field(
        alias="amount_total",
    )
    """
    Total after discounts and taxes are applied.
    """
    line_items: typing.Optional["QuotesResourceUpfrontLineItems"] = pydantic.Field(
        alias="line_items", default=None
    )
    """
    The line items that will appear on the next invoice after this quote is accepted. This does not include pending invoice items that exist on the customer but may still be included in the next invoice.
    """
    total_details: "QuotesResourceTotalDetails" = pydantic.Field(
        alias="total_details",
    )
