import pydantic
import typing


class AccountDashboardSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    display_name: typing.Optional[str] = pydantic.Field(
        alias="display_name", default=None
    )
    """
    The display name for this account. This is used on the Stripe Dashboard to differentiate between accounts.
    """
    timezone: typing.Optional[str] = pydantic.Field(alias="timezone", default=None)
    """
    The timezone used in the Stripe Dashboard for this account. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones).
    """
