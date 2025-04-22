import pydantic
import typing
import typing_extensions

from .customer_source_update_body_owner_address import (
    CustomerSourceUpdateBodyOwnerAddress,
    _SerializerCustomerSourceUpdateBodyOwnerAddress,
)


class CustomerSourceUpdateBodyOwner(typing_extensions.TypedDict):
    """
    CustomerSourceUpdateBodyOwner
    """

    address: typing_extensions.NotRequired[CustomerSourceUpdateBodyOwnerAddress]

    email: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]


class _SerializerCustomerSourceUpdateBodyOwner(pydantic.BaseModel):
    """
    Serializer for CustomerSourceUpdateBodyOwner handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[_SerializerCustomerSourceUpdateBodyOwnerAddress] = (
        pydantic.Field(alias="address", default=None)
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
