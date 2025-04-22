import pydantic
import typing
import typing_extensions

from .customer_bank_account_update_body_owner_address import (
    CustomerBankAccountUpdateBodyOwnerAddress,
    _SerializerCustomerBankAccountUpdateBodyOwnerAddress,
)


class CustomerBankAccountUpdateBodyOwner(typing_extensions.TypedDict):
    """
    CustomerBankAccountUpdateBodyOwner
    """

    address: typing_extensions.NotRequired[CustomerBankAccountUpdateBodyOwnerAddress]

    email: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]


class _SerializerCustomerBankAccountUpdateBodyOwner(pydantic.BaseModel):
    """
    Serializer for CustomerBankAccountUpdateBodyOwner handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[_SerializerCustomerBankAccountUpdateBodyOwnerAddress] = (
        pydantic.Field(alias="address", default=None)
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
