import pydantic
import typing

from .address import Address


class TreasurySharedResourceBillingDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: Address = pydantic.Field(
        alias="address",
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Email address.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Full name.
    """
