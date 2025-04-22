import pydantic
import typing
import typing_extensions

from .issuing_card_create_body_shipping_address import (
    IssuingCardCreateBodyShippingAddress,
    _SerializerIssuingCardCreateBodyShippingAddress,
)
from .issuing_card_create_body_shipping_address_validation import (
    IssuingCardCreateBodyShippingAddressValidation,
    _SerializerIssuingCardCreateBodyShippingAddressValidation,
)
from .issuing_card_create_body_shipping_customs import (
    IssuingCardCreateBodyShippingCustoms,
    _SerializerIssuingCardCreateBodyShippingCustoms,
)


class IssuingCardCreateBodyShipping(typing_extensions.TypedDict):
    """
    The address where the card will be shipped.
    """

    address: typing_extensions.Required[IssuingCardCreateBodyShippingAddress]

    address_validation: typing_extensions.NotRequired[
        IssuingCardCreateBodyShippingAddressValidation
    ]

    customs: typing_extensions.NotRequired[IssuingCardCreateBodyShippingCustoms]

    name: typing_extensions.Required[str]

    phone_number: typing_extensions.NotRequired[str]

    require_signature: typing_extensions.NotRequired[bool]

    service: typing_extensions.NotRequired[
        typing_extensions.Literal["express", "priority", "standard"]
    ]

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["bulk", "individual"]
    ]


class _SerializerIssuingCardCreateBodyShipping(pydantic.BaseModel):
    """
    Serializer for IssuingCardCreateBodyShipping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerIssuingCardCreateBodyShippingAddress = pydantic.Field(
        alias="address",
    )
    address_validation: typing.Optional[
        _SerializerIssuingCardCreateBodyShippingAddressValidation
    ] = pydantic.Field(alias="address_validation", default=None)
    customs: typing.Optional[_SerializerIssuingCardCreateBodyShippingCustoms] = (
        pydantic.Field(alias="customs", default=None)
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="phone_number", default=None
    )
    require_signature: typing.Optional[bool] = pydantic.Field(
        alias="require_signature", default=None
    )
    service: typing.Optional[
        typing_extensions.Literal["express", "priority", "standard"]
    ] = pydantic.Field(alias="service", default=None)
    type_: typing.Optional[typing_extensions.Literal["bulk", "individual"]] = (
        pydantic.Field(alias="type", default=None)
    )
