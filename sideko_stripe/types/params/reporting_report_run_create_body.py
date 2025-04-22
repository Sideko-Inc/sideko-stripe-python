import pydantic
import typing
import typing_extensions

from .reporting_report_run_create_body_parameters import (
    ReportingReportRunCreateBodyParameters,
    _SerializerReportingReportRunCreateBodyParameters,
)


class ReportingReportRunCreateBody(typing_extensions.TypedDict, total=False):
    """
    ReportingReportRunCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    parameters: typing_extensions.NotRequired[ReportingReportRunCreateBodyParameters]
    """
    Parameters specifying how the report should be run. Different Report Types have different required and optional parameters, listed in the [API Access to Reports](https://stripe.com/docs/reporting/statements/api) documentation.
    """

    report_type: typing_extensions.Required[str]
    """
    The ID of the [report type](https://stripe.com/docs/reporting/statements/api#report-types) to run, such as `"balance.summary.1"`.
    """


class _SerializerReportingReportRunCreateBody(pydantic.BaseModel):
    """
    Serializer for ReportingReportRunCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    parameters: typing.Optional[_SerializerReportingReportRunCreateBodyParameters] = (
        pydantic.Field(alias="parameters", default=None)
    )
    report_type: str = pydantic.Field(
        alias="report_type",
    )
