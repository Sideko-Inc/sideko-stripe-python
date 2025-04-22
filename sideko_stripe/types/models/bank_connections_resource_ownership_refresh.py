import pydantic
import typing
import typing_extensions


class BankConnectionsResourceOwnershipRefresh(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    last_attempted_at: int = pydantic.Field(
        alias="last_attempted_at",
    )
    """
    The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch.
    """
    next_refresh_available_at: typing.Optional[int] = pydantic.Field(
        alias="next_refresh_available_at", default=None
    )
    """
    Time at which the next ownership refresh can be initiated. This value will be `null` when `status` is `pending`. Measured in seconds since the Unix epoch.
    """
    status: typing_extensions.Literal["failed", "pending", "succeeded"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The status of the last refresh attempt.
    """
