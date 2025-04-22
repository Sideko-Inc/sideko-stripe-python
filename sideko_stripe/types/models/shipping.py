import pydantic
import typing

from .address import Address


class Shipping(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    carrier: typing.Optional[str] = pydantic.Field(alias="carrier", default=None)
    """
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Recipient name.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Recipient phone (including extension).
    """
    tracking_number: typing.Optional[str] = pydantic.Field(
        alias="tracking_number", default=None
    )
    """
    The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
    """
