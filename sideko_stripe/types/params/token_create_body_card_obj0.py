import pydantic
import typing
import typing_extensions

from .token_create_body_card_obj0_networks import (
    TokenCreateBodyCardObj0Networks,
    _SerializerTokenCreateBodyCardObj0Networks,
)


class TokenCreateBodyCardObj0(typing_extensions.TypedDict):
    """
    TokenCreateBodyCardObj0
    """

    address_city: typing_extensions.NotRequired[str]

    address_country: typing_extensions.NotRequired[str]

    address_line1: typing_extensions.NotRequired[str]

    address_line2: typing_extensions.NotRequired[str]

    address_state: typing_extensions.NotRequired[str]

    address_zip: typing_extensions.NotRequired[str]

    currency: typing_extensions.NotRequired[str]

    cvc: typing_extensions.NotRequired[str]

    exp_month: typing_extensions.Required[str]

    exp_year: typing_extensions.Required[str]

    name: typing_extensions.NotRequired[str]

    networks: typing_extensions.NotRequired[TokenCreateBodyCardObj0Networks]

    number: typing_extensions.Required[str]


class _SerializerTokenCreateBodyCardObj0(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyCardObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address_city: typing.Optional[str] = pydantic.Field(
        alias="address_city", default=None
    )
    address_country: typing.Optional[str] = pydantic.Field(
        alias="address_country", default=None
    )
    address_line1: typing.Optional[str] = pydantic.Field(
        alias="address_line1", default=None
    )
    address_line2: typing.Optional[str] = pydantic.Field(
        alias="address_line2", default=None
    )
    address_state: typing.Optional[str] = pydantic.Field(
        alias="address_state", default=None
    )
    address_zip: typing.Optional[str] = pydantic.Field(
        alias="address_zip", default=None
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    cvc: typing.Optional[str] = pydantic.Field(alias="cvc", default=None)
    exp_month: str = pydantic.Field(
        alias="exp_month",
    )
    exp_year: str = pydantic.Field(
        alias="exp_year",
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    networks: typing.Optional[_SerializerTokenCreateBodyCardObj0Networks] = (
        pydantic.Field(alias="networks", default=None)
    )
    number: str = pydantic.Field(
        alias="number",
    )
