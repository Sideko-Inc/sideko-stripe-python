import pydantic
import typing_extensions


class SubscriptionPendingInvoiceItemInterval(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    interval: typing_extensions.Literal["day", "month", "week", "year"] = (
        pydantic.Field(
            alias="interval",
        )
    )
    """
    Specifies invoicing frequency. Either `day`, `week`, `month` or `year`.
    """
    interval_count: int = pydantic.Field(
        alias="interval_count",
    )
    """
    The number of intervals between invoices. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
    """
