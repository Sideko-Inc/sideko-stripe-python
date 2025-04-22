import pydantic
import typing
import typing_extensions

from .charge_create_body_shipping_address import (
    ChargeCreateBodyShippingAddress,
    _SerializerChargeCreateBodyShippingAddress,
)


class ChargeCreateBodyShipping(typing_extensions.TypedDict):
    """
    Shipping information for the charge. Helps prevent fraud on charges for physical goods.
    """

    address: typing_extensions.Required[ChargeCreateBodyShippingAddress]

    carrier: typing_extensions.NotRequired[str]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[str]

    tracking_number: typing_extensions.NotRequired[str]


class _SerializerChargeCreateBodyShipping(pydantic.BaseModel):
    """
    Serializer for ChargeCreateBodyShipping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerChargeCreateBodyShippingAddress = pydantic.Field(
        alias="address",
    )
    carrier: typing.Optional[str] = pydantic.Field(alias="carrier", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    tracking_number: typing.Optional[str] = pydantic.Field(
        alias="tracking_number", default=None
    )
