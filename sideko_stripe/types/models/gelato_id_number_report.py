import pydantic
import typing
import typing_extensions

from .gelato_data_id_number_report_date import GelatoDataIdNumberReportDate
from .gelato_id_number_report_error import GelatoIdNumberReportError


class GelatoIdNumberReport(pydantic.BaseModel):
    """
    Result from an id_number check
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    dob: typing.Optional[GelatoDataIdNumberReportDate] = pydantic.Field(
        alias="dob", default=None
    )
    """
    Point in Time
    """
    error: typing.Optional[GelatoIdNumberReportError] = pydantic.Field(
        alias="error", default=None
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    """
    First name.
    """
    id_number: typing.Optional[str] = pydantic.Field(alias="id_number", default=None)
    """
    ID number. When `id_number_type` is `us_ssn`, only the last 4 digits are present.
    """
    id_number_type: typing.Optional[
        typing_extensions.Literal["br_cpf", "sg_nric", "us_ssn"]
    ] = pydantic.Field(alias="id_number_type", default=None)
    """
    Type of ID number.
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    """
    Last name.
    """
    status: typing_extensions.Literal["unverified", "verified"] = pydantic.Field(
        alias="status",
    )
    """
    Status of this `id_number` check.
    """
