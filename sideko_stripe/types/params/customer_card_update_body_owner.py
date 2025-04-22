import pydantic
import typing
import typing_extensions

from .customer_card_update_body_owner_address import (
    CustomerCardUpdateBodyOwnerAddress,
    _SerializerCustomerCardUpdateBodyOwnerAddress,
)


class CustomerCardUpdateBodyOwner(typing_extensions.TypedDict):
    """
    CustomerCardUpdateBodyOwner
    """

    address: typing_extensions.NotRequired[CustomerCardUpdateBodyOwnerAddress]

    email: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]


class _SerializerCustomerCardUpdateBodyOwner(pydantic.BaseModel):
    """
    Serializer for CustomerCardUpdateBodyOwner handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[_SerializerCustomerCardUpdateBodyOwnerAddress] = (
        pydantic.Field(alias="address", default=None)
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
