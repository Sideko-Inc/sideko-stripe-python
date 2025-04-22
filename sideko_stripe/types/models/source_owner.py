import pydantic
import typing

from .address import Address


class SourceOwner(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    Owner's email address.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Owner's full name.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Owner's phone number (including extension).
    """
    verified_address: typing.Optional[Address] = pydantic.Field(
        alias="verified_address", default=None
    )
    verified_email: typing.Optional[str] = pydantic.Field(
        alias="verified_email", default=None
    )
    """
    Verified owner's email address. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.
    """
    verified_name: typing.Optional[str] = pydantic.Field(
        alias="verified_name", default=None
    )
    """
    Verified owner's full name. Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.
    """
    verified_phone: typing.Optional[str] = pydantic.Field(
        alias="verified_phone", default=None
    )
    """
    Verified owner's phone number (including extension). Verified values are verified or provided by the payment method directly (and if supported) at the time of authorization or settlement. They cannot be set or mutated.
    """
