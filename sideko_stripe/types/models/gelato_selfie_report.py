import pydantic
import typing
import typing_extensions

from .gelato_selfie_report_error import GelatoSelfieReportError


class GelatoSelfieReport(pydantic.BaseModel):
    """
    Result from a selfie check
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    document: typing.Optional[str] = pydantic.Field(alias="document", default=None)
    """
    ID of the [File](https://stripe.com/docs/api/files) holding the image of the identity document used in this check.
    """
    error: typing.Optional[GelatoSelfieReportError] = pydantic.Field(
        alias="error", default=None
    )
    selfie: typing.Optional[str] = pydantic.Field(alias="selfie", default=None)
    """
    ID of the [File](https://stripe.com/docs/api/files) holding the image of the selfie used in this check.
    """
    status: typing_extensions.Literal["unverified", "verified"] = pydantic.Field(
        alias="status",
    )
    """
    Status of this `selfie` check.
    """
