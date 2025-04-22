import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .quotes_resource_total_details_resource_breakdown import (
        QuotesResourceTotalDetailsResourceBreakdown,
    )


class QuotesResourceTotalDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_discount: int = pydantic.Field(
        alias="amount_discount",
    )
    """
    This is the sum of all the discounts.
    """
    amount_shipping: typing.Optional[int] = pydantic.Field(
        alias="amount_shipping", default=None
    )
    """
    This is the sum of all the shipping amounts.
    """
    amount_tax: int = pydantic.Field(
        alias="amount_tax",
    )
    """
    This is the sum of all the tax amounts.
    """
    breakdown: typing.Optional["QuotesResourceTotalDetailsResourceBreakdown"] = (
        pydantic.Field(alias="breakdown", default=None)
    )
