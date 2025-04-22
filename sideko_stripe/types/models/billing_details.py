import pydantic
import typing

from .address import Address


class BillingDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Email address.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Full name.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Billing phone number (including extension).
    """
