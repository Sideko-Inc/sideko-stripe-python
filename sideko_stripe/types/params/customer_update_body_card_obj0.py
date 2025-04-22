import pydantic
import typing
import typing_extensions

from .customer_update_body_card_obj0_metadata import (
    CustomerUpdateBodyCardObj0Metadata,
    _SerializerCustomerUpdateBodyCardObj0Metadata,
)


class CustomerUpdateBodyCardObj0(typing_extensions.TypedDict):
    """
    CustomerUpdateBodyCardObj0
    """

    address_city: typing_extensions.NotRequired[str]

    address_country: typing_extensions.NotRequired[str]

    address_line1: typing_extensions.NotRequired[str]

    address_line2: typing_extensions.NotRequired[str]

    address_state: typing_extensions.NotRequired[str]

    address_zip: typing_extensions.NotRequired[str]

    cvc: typing_extensions.NotRequired[str]

    exp_month: typing_extensions.Required[int]

    exp_year: typing_extensions.Required[int]

    metadata: typing_extensions.NotRequired[CustomerUpdateBodyCardObj0Metadata]

    name: typing_extensions.NotRequired[str]

    number: typing_extensions.Required[str]

    object: typing_extensions.NotRequired[typing_extensions.Literal["card"]]


class _SerializerCustomerUpdateBodyCardObj0(pydantic.BaseModel):
    """
    Serializer for CustomerUpdateBodyCardObj0 handling case conversions
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
    cvc: typing.Optional[str] = pydantic.Field(alias="cvc", default=None)
    exp_month: int = pydantic.Field(
        alias="exp_month",
    )
    exp_year: int = pydantic.Field(
        alias="exp_year",
    )
    metadata: typing.Optional[_SerializerCustomerUpdateBodyCardObj0Metadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    number: str = pydantic.Field(
        alias="number",
    )
    object: typing.Optional[typing_extensions.Literal["card"]] = pydantic.Field(
        alias="object", default=None
    )
