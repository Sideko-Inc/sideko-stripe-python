import pydantic
import typing
import typing_extensions

from .gelato_phone_report_error import GelatoPhoneReportError


class GelatoPhoneReport(pydantic.BaseModel):
    """
    Result from a phone check
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    error: typing.Optional[GelatoPhoneReportError] = pydantic.Field(
        alias="error", default=None
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Phone to be verified.
    """
    status: typing_extensions.Literal["unverified", "verified"] = pydantic.Field(
        alias="status",
    )
    """
    Status of this `phone` check.
    """
