import pydantic
import typing
import typing_extensions

from .address import Address
from .gelato_data_verified_outputs_date import GelatoDataVerifiedOutputsDate


class GelatoVerifiedOutputs(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    dob: typing.Optional[GelatoDataVerifiedOutputsDate] = pydantic.Field(
        alias="dob", default=None
    )
    """
    Point in Time
    """
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The user's verified email address
    """
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    """
    The user's verified first name.
    """
    id_number: typing.Optional[str] = pydantic.Field(alias="id_number", default=None)
    """
    The user's verified id number.
    """
    id_number_type: typing.Optional[
        typing_extensions.Literal["br_cpf", "sg_nric", "us_ssn"]
    ] = pydantic.Field(alias="id_number_type", default=None)
    """
    The user's verified id number type.
    """
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    """
    The user's verified last name.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    The user's verified phone number
    """
