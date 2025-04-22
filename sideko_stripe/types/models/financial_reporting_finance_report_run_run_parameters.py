import pydantic
import typing


class FinancialReportingFinanceReportRunRunParameters(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    columns: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="columns", default=None
    )
    """
    The set of output columns requested for inclusion in the report run.
    """
    connected_account: typing.Optional[str] = pydantic.Field(
        alias="connected_account", default=None
    )
    """
    Connected account ID by which to filter the report run.
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    Currency of objects to be included in the report run.
    """
    interval_end: typing.Optional[int] = pydantic.Field(
        alias="interval_end", default=None
    )
    """
    Ending timestamp of data to be included in the report run. Can be any UTC timestamp between 1 second after the user specified `interval_start` and 1 second before this report's last `data_available_end` value.
    """
    interval_start: typing.Optional[int] = pydantic.Field(
        alias="interval_start", default=None
    )
    """
    Starting timestamp of data to be included in the report run. Can be any UTC timestamp between 1 second after this report's `data_available_start` and 1 second before the user specified `interval_end` value.
    """
    payout: typing.Optional[str] = pydantic.Field(alias="payout", default=None)
    """
    Payout ID by which to filter the report run.
    """
    reporting_category: typing.Optional[str] = pydantic.Field(
        alias="reporting_category", default=None
    )
    """
    Category of balance transactions to be included in the report run.
    """
    timezone: typing.Optional[str] = pydantic.Field(alias="timezone", default=None)
    """
    Defaults to `Etc/UTC`. The output timezone for all timestamps in the report. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones). Has no effect on `interval_start` or `interval_end`.
    """
