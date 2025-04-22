import pydantic
import typing


class TransferSchedule(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    delay_days: int = pydantic.Field(
        alias="delay_days",
    )
    """
    The number of days charges for the account will be held before being paid out.
    """
    interval: str = pydantic.Field(
        alias="interval",
    )
    """
    How frequently funds will be paid out. One of `manual` (payouts only created via API call), `daily`, `weekly`, or `monthly`.
    """
    monthly_anchor: typing.Optional[int] = pydantic.Field(
        alias="monthly_anchor", default=None
    )
    """
    The day of the month funds will be paid out. Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st of the month are sent on the last day of shorter months.
    """
    weekly_anchor: typing.Optional[str] = pydantic.Field(
        alias="weekly_anchor", default=None
    )
    """
    The day of the week funds will be paid out, of the style 'monday', 'tuesday', etc. Only shown if `interval` is weekly.
    """
