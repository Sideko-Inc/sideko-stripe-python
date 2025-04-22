import pydantic
import typing
import typing_extensions


class Recurring(pydantic.BaseModel):
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
    The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.
    """
    interval_count: int = pydantic.Field(
        alias="interval_count",
    )
    """
    The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.
    """
    meter: typing.Optional[str] = pydantic.Field(alias="meter", default=None)
    """
    The meter tracking the usage of a metered price
    """
    usage_type: typing_extensions.Literal["licensed", "metered"] = pydantic.Field(
        alias="usage_type",
    )
    """
    Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`.
    """
