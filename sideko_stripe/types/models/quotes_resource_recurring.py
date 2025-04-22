import pydantic
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .quotes_resource_total_details import QuotesResourceTotalDetails


class QuotesResourceRecurring(pydantic.BaseModel):
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
    interval: typing_extensions.Literal["day", "month", "week", "year"] = (
        pydantic.Field(
            alias="interval",
        )
    )
    """
    The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.
    """
    interval_count: int = pydantic.Field(
        alias="interval_count",
    )
    """
    The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.
    """
    total_details: "QuotesResourceTotalDetails" = pydantic.Field(
        alias="total_details",
    )
