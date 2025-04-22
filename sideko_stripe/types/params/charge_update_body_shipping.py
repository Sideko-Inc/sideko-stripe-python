import pydantic
import typing
import typing_extensions

from .charge_update_body_shipping_address import (
    ChargeUpdateBodyShippingAddress,
    _SerializerChargeUpdateBodyShippingAddress,
)


class ChargeUpdateBodyShipping(typing_extensions.TypedDict):
    """
    Shipping information for the charge. Helps prevent fraud on charges for physical goods.
    """

    address: typing_extensions.Required[ChargeUpdateBodyShippingAddress]

    carrier: typing_extensions.NotRequired[str]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[str]

    tracking_number: typing_extensions.NotRequired[str]


class _SerializerChargeUpdateBodyShipping(pydantic.BaseModel):
    """
    Serializer for ChargeUpdateBodyShipping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerChargeUpdateBodyShippingAddress = pydantic.Field(
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
