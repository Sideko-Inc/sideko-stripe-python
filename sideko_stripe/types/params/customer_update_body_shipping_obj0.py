import pydantic
import typing
import typing_extensions

from .customer_update_body_shipping_obj0_address import (
    CustomerUpdateBodyShippingObj0Address,
    _SerializerCustomerUpdateBodyShippingObj0Address,
)


class CustomerUpdateBodyShippingObj0(typing_extensions.TypedDict):
    """
    CustomerUpdateBodyShippingObj0
    """

    address: typing_extensions.Required[CustomerUpdateBodyShippingObj0Address]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[str]


class _SerializerCustomerUpdateBodyShippingObj0(pydantic.BaseModel):
    """
    Serializer for CustomerUpdateBodyShippingObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerCustomerUpdateBodyShippingObj0Address = pydantic.Field(
        alias="address",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
