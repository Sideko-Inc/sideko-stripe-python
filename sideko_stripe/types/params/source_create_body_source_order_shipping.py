import pydantic
import typing
import typing_extensions

from .source_create_body_source_order_shipping_address import (
    SourceCreateBodySourceOrderShippingAddress,
    _SerializerSourceCreateBodySourceOrderShippingAddress,
)


class SourceCreateBodySourceOrderShipping(typing_extensions.TypedDict):
    """
    SourceCreateBodySourceOrderShipping
    """

    address: typing_extensions.Required[SourceCreateBodySourceOrderShippingAddress]

    carrier: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]

    tracking_number: typing_extensions.NotRequired[str]


class _SerializerSourceCreateBodySourceOrderShipping(pydantic.BaseModel):
    """
    Serializer for SourceCreateBodySourceOrderShipping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerSourceCreateBodySourceOrderShippingAddress = pydantic.Field(
        alias="address",
    )
    carrier: typing.Optional[str] = pydantic.Field(alias="carrier", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    tracking_number: typing.Optional[str] = pydantic.Field(
        alias="tracking_number", default=None
    )
