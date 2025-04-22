import pydantic
import typing
import typing_extensions


class ReportingReportType(pydantic.BaseModel):
    """
    The Report Type resource corresponds to a particular type of report, such as
    the "Activity summary" or "Itemized payouts" reports. These objects are
    identified by an ID belonging to a set of enumerated values. See
    [API Access to Reports documentation](https://stripe.com/docs/reporting/statements/api)
    for those Report Type IDs, along with required and optional parameters.

    Note that certain report types can only be run based on your live-mode data (not test-mode
    data), and will error when queried without a [live-mode API key](https://stripe.com/docs/keys#test-live-modes).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data_available_end: int = pydantic.Field(
        alias="data_available_end",
    )
    """
    Most recent time for which this Report Type is available. Measured in seconds since the Unix epoch.
    """
    data_available_start: int = pydantic.Field(
        alias="data_available_start",
    )
    """
    Earliest time for which this Report Type is available. Measured in seconds since the Unix epoch.
    """
    default_columns: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="default_columns", default=None
    )
    """
    List of column names that are included by default when this Report Type gets run. (If the Report Type doesn't support the `columns` parameter, this will be null.)
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The [ID of the Report Type](https://stripe.com/docs/reporting/statements/api#available-report-types), such as `balance.summary.1`.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    Human-readable name of the Report Type
    """
    object: typing_extensions.Literal["reporting.report_type"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    updated: int = pydantic.Field(
        alias="updated",
    )
    """
    When this Report Type was latest updated. Measured in seconds since the Unix epoch.
    """
    version: int = pydantic.Field(
        alias="version",
    )
    """
    Version of the Report Type. Different versions report with the same ID will have the same purpose, but may take different run parameters or have different result schemas.
    """
