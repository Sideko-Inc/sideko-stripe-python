import pydantic
import typing
import typing_extensions

from .gelato_email_report_error import GelatoEmailReportError


class GelatoEmailReport(pydantic.BaseModel):
    """
    Result from a email check
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Email to be verified.
    """
    error: typing.Optional[GelatoEmailReportError] = pydantic.Field(
        alias="error", default=None
    )
    status: typing_extensions.Literal["unverified", "verified"] = pydantic.Field(
        alias="status",
    )
    """
    Status of this `email` check.
    """
