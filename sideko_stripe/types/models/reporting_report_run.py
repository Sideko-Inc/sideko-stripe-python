import pydantic
import typing
import typing_extensions

from .financial_reporting_finance_report_run_run_parameters import (
    FinancialReportingFinanceReportRunRunParameters,
)

if typing_extensions.TYPE_CHECKING:
    from .file import File


class ReportingReportRun(pydantic.BaseModel):
    """
    The Report Run object represents an instance of a report type generated with
    specific run parameters. Once the object is created, Stripe begins processing the report.
    When the report has finished running, it will give you a reference to a file
    where you can retrieve your results. For an overview, see
    [API Access to Reports](https://stripe.com/docs/reporting/statements/api).

    Note that certain report types can only be run based on your live-mode data (not test-mode
    data), and will error when queried without a [live-mode API key](https://stripe.com/docs/keys#test-live-modes).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    error: typing.Optional[str] = pydantic.Field(alias="error", default=None)
    """
    If something should go wrong during the run, a message about the failure (populated when
     `status=failed`).
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    `true` if the report is run on live mode data and `false` if it is run on test mode data.
    """
    object: typing_extensions.Literal["reporting.report_run"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    parameters: FinancialReportingFinanceReportRunRunParameters = pydantic.Field(
        alias="parameters",
    )
    report_type: str = pydantic.Field(
        alias="report_type",
    )
    """
    The ID of the [report type](https://stripe.com/docs/reports/report-types) to run, such as `"balance.summary.1"`.
    """
    result: typing.Optional["File"] = pydantic.Field(alias="result", default=None)
    """
    This object represents files hosted on Stripe's servers. You can upload
    files with the [create file](https://stripe.com/docs/api#create_file) request
    (for example, when uploading dispute evidence). Stripe also
    creates files independently (for example, the results of a [Sigma scheduled
    query](#scheduled_queries)).
    
    Related guide: [File upload guide](https://stripe.com/docs/file-upload)
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    Status of this report run. This will be `pending` when the run is initially created.
     When the run finishes, this will be set to `succeeded` and the `result` field will be populated.
     Rarely, we may encounter an error, at which point this will be set to `failed` and the `error` field will be populated.
    """
    succeeded_at: typing.Optional[int] = pydantic.Field(
        alias="succeeded_at", default=None
    )
    """
    Timestamp at which this run successfully finished (populated when
     `status=succeeded`). Measured in seconds since the Unix epoch.
    """
