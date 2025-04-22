import pydantic
import typing
import typing_extensions

from .address import Address
from .issuing_card_shipping_address_validation import (
    IssuingCardShippingAddressValidation,
)
from .issuing_card_shipping_customs import IssuingCardShippingCustoms


class IssuingCardShipping(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: Address = pydantic.Field(
        alias="address",
    )
    address_validation: typing.Optional[IssuingCardShippingAddressValidation] = (
        pydantic.Field(alias="address_validation", default=None)
    )
    carrier: typing.Optional[
        typing_extensions.Literal["dhl", "fedex", "royal_mail", "usps"]
    ] = pydantic.Field(alias="carrier", default=None)
    """
    The delivery company that shipped a card.
    """
    customs: typing.Optional[IssuingCardShippingCustoms] = pydantic.Field(
        alias="customs", default=None
    )
    eta: typing.Optional[int] = pydantic.Field(alias="eta", default=None)
    """
    A unix timestamp representing a best estimate of when the card will be delivered.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    Recipient name.
    """
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="phone_number", default=None
    )
    """
    The phone number of the receiver of the shipment. Our courier partners will use this number to contact you in the event of card delivery issues. For individual shipments to the EU/UK, if this field is empty, we will provide them with the phone number provided when the cardholder was initially created.
    """
    require_signature: typing.Optional[bool] = pydantic.Field(
        alias="require_signature", default=None
    )
    """
    Whether a signature is required for card delivery. This feature is only supported for US users. Standard shipping service does not support signature on delivery. The default value for standard shipping service is false and for express and priority services is true.
    """
    service: typing_extensions.Literal["express", "priority", "standard"] = (
        pydantic.Field(
            alias="service",
        )
    )
    """
    Shipment service, such as `standard` or `express`.
    """
    status: typing.Optional[
        typing_extensions.Literal[
            "canceled",
            "delivered",
            "failure",
            "pending",
            "returned",
            "shipped",
            "submitted",
        ]
    ] = pydantic.Field(alias="status", default=None)
    """
    The delivery status of the card.
    """
    tracking_number: typing.Optional[str] = pydantic.Field(
        alias="tracking_number", default=None
    )
    """
    A tracking number for a card shipment.
    """
    tracking_url: typing.Optional[str] = pydantic.Field(
        alias="tracking_url", default=None
    )
    """
    A link to the shipping carrier's site where you can view detailed information about a card shipment.
    """
    type_: typing_extensions.Literal["bulk", "individual"] = pydantic.Field(
        alias="type",
    )
    """
    Packaging options.
    """
