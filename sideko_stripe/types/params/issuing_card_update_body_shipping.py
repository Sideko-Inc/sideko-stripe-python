import pydantic
import typing
import typing_extensions

from .issuing_card_update_body_shipping_address import (
    IssuingCardUpdateBodyShippingAddress,
    _SerializerIssuingCardUpdateBodyShippingAddress,
)
from .issuing_card_update_body_shipping_address_validation import (
    IssuingCardUpdateBodyShippingAddressValidation,
    _SerializerIssuingCardUpdateBodyShippingAddressValidation,
)
from .issuing_card_update_body_shipping_customs import (
    IssuingCardUpdateBodyShippingCustoms,
    _SerializerIssuingCardUpdateBodyShippingCustoms,
)


class IssuingCardUpdateBodyShipping(typing_extensions.TypedDict):
    """
    Updated shipping information for the card.
    """

    address: typing_extensions.Required[IssuingCardUpdateBodyShippingAddress]

    address_validation: typing_extensions.NotRequired[
        IssuingCardUpdateBodyShippingAddressValidation
    ]

    customs: typing_extensions.NotRequired[IssuingCardUpdateBodyShippingCustoms]

    name: typing_extensions.Required[str]

    phone_number: typing_extensions.NotRequired[str]

    require_signature: typing_extensions.NotRequired[bool]

    service: typing_extensions.NotRequired[
        typing_extensions.Literal["express", "priority", "standard"]
    ]

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["bulk", "individual"]
    ]


class _SerializerIssuingCardUpdateBodyShipping(pydantic.BaseModel):
    """
    Serializer for IssuingCardUpdateBodyShipping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerIssuingCardUpdateBodyShippingAddress = pydantic.Field(
        alias="address",
    )
    address_validation: typing.Optional[
        _SerializerIssuingCardUpdateBodyShippingAddressValidation
    ] = pydantic.Field(alias="address_validation", default=None)
    customs: typing.Optional[_SerializerIssuingCardUpdateBodyShippingCustoms] = (
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
