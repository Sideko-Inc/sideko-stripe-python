import pydantic
import typing
import typing_extensions

from .address import Address
from .gelato_data_document_report_date_of_birth import (
    GelatoDataDocumentReportDateOfBirth,
)
from .gelato_data_document_report_expiration_date import (
    GelatoDataDocumentReportExpirationDate,
)
from .gelato_data_document_report_issued_date import GelatoDataDocumentReportIssuedDate
from .gelato_document_report_error import GelatoDocumentReportError


class GelatoDocumentReport(pydantic.BaseModel):
    """
    Result from a document check
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    dob: typing.Optional[GelatoDataDocumentReportDateOfBirth] = pydantic.Field(
        alias="dob", default=None
    )
    """
    Point in Time
    """
    error: typing.Optional[GelatoDocumentReportError] = pydantic.Field(
        alias="error", default=None
    )
    expiration_date: typing.Optional[GelatoDataDocumentReportExpirationDate] = (
        pydantic.Field(alias="expiration_date", default=None)
    )
    """
    Point in Time
    """
    files: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="files", default=None
    )
    """
    Array of [File](https://stripe.com/docs/api/files) ids containing images for this document.
    """
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    """
    First name as it appears in the document.
    """
    issued_date: typing.Optional[GelatoDataDocumentReportIssuedDate] = pydantic.Field(
        alias="issued_date", default=None
    )
    """
    Point in Time
    """
    issuing_country: typing.Optional[str] = pydantic.Field(
        alias="issuing_country", default=None
    )
    """
    Issuing country of the document.
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    """
    Last name as it appears in the document.
    """
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    """
    Document ID number.
    """
    status: typing_extensions.Literal["unverified", "verified"] = pydantic.Field(
        alias="status",
    )
    """
    Status of this `document` check.
    """
    type_: typing.Optional[
        typing_extensions.Literal["driving_license", "id_card", "passport"]
    ] = pydantic.Field(alias="type", default=None)
    """
    Type of the document.
    """
