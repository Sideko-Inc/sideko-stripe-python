import pydantic
import typing
import typing_extensions

from .customer_create_body_shipping_obj0_address import (
    CustomerCreateBodyShippingObj0Address,
    _SerializerCustomerCreateBodyShippingObj0Address,
)


class CustomerCreateBodyShippingObj0(typing_extensions.TypedDict):
    """
    CustomerCreateBodyShippingObj0
    """

    address: typing_extensions.Required[CustomerCreateBodyShippingObj0Address]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[str]


class _SerializerCustomerCreateBodyShippingObj0(pydantic.BaseModel):
    """
    Serializer for CustomerCreateBodyShippingObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerCustomerCreateBodyShippingObj0Address = pydantic.Field(
        alias="address",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
