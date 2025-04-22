import pydantic
import typing
import typing_extensions

from .sigma_scheduled_query_run_error import SigmaScheduledQueryRunError

if typing_extensions.TYPE_CHECKING:
    from .file import File


class ScheduledQueryRun(pydantic.BaseModel):
    """
    If you have [scheduled a Sigma query](https://stripe.com/docs/sigma/scheduled-queries), you'll
    receive a `sigma.scheduled_query_run.created` webhook each time the query
    runs. The webhook contains a `ScheduledQueryRun` object, which you can use to
    retrieve the query results.
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
    data_load_time: int = pydantic.Field(
        alias="data_load_time",
    )
    """
    When the query was run, Sigma contained a snapshot of your Stripe data at this time.
    """
    error: typing.Optional[SigmaScheduledQueryRunError] = pydantic.Field(
        alias="error", default=None
    )
    file: typing.Optional["File"] = pydantic.Field(alias="file", default=None)
    """
    This object represents files hosted on Stripe's servers. You can upload
    files with the [create file](https://stripe.com/docs/api#create_file) request
    (for example, when uploading dispute evidence). Stripe also
    creates files independently (for example, the results of a [Sigma scheduled
    query](#scheduled_queries)).
    
    Related guide: [File upload guide](https://stripe.com/docs/file-upload)
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
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["scheduled_query_run"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    result_available_until: int = pydantic.Field(
        alias="result_available_until",
    )
    """
    Time at which the result expires and is no longer available for download.
    """
    sql: str = pydantic.Field(
        alias="sql",
    )
    """
    SQL for the query.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The query's execution status, which will be `completed` for successful runs, and `canceled`, `failed`, or `timed_out` otherwise.
    """
    title: str = pydantic.Field(
        alias="title",
    )
    """
    Title of the query.
    """
