import pydantic
import typing
import typing_extensions

from .customer_source_update_body_metadata_obj0 import (
    CustomerSourceUpdateBodyMetadataObj0,
    _SerializerCustomerSourceUpdateBodyMetadataObj0,
)
from .customer_source_update_body_owner import (
    CustomerSourceUpdateBodyOwner,
    _SerializerCustomerSourceUpdateBodyOwner,
)


class CustomerSourceUpdateBody(typing_extensions.TypedDict, total=False):
    """
    CustomerSourceUpdateBody
    """

    account_holder_name: typing_extensions.NotRequired[str]
    """
    The name of the person or business that owns the bank account.
    """

    account_holder_type: typing_extensions.NotRequired[
        typing_extensions.Literal["company", "individual"]
    ]
    """
    The type of entity that holds the account. This can be either `individual` or `company`.
    """

    address_city: typing_extensions.NotRequired[str]
    """
    City/District/Suburb/Town/Village.
    """

    address_country: typing_extensions.NotRequired[str]
    """
    Billing address country, if provided when creating card.
    """

    address_line1: typing_extensions.NotRequired[str]
    """
    Address line 1 (Street address/PO Box/Company name).
    """

    address_line2: typing_extensions.NotRequired[str]
    """
    Address line 2 (Apartment/Suite/Unit/Building).
    """

    address_state: typing_extensions.NotRequired[str]
    """
    State/County/Province/Region.
    """

    address_zip: typing_extensions.NotRequired[str]
    """
    ZIP or postal code.
    """

    exp_month: typing_extensions.NotRequired[str]
    """
    Two digit number representing the card’s expiration month.
    """

    exp_year: typing_extensions.NotRequired[str]
    """
    Four digit number representing the card’s expiration year.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[CustomerSourceUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    name: typing_extensions.NotRequired[str]
    """
    Cardholder name.
    """

    owner: typing_extensions.NotRequired[CustomerSourceUpdateBodyOwner]


class _SerializerCustomerSourceUpdateBody(pydantic.BaseModel):
    """
    Serializer for CustomerSourceUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="account_holder_name", default=None
    )
    account_holder_type: typing.Optional[
        typing_extensions.Literal["company", "individual"]
    ] = pydantic.Field(alias="account_holder_type", default=None)
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
    exp_month: typing.Optional[str] = pydantic.Field(alias="exp_month", default=None)
    exp_year: typing.Optional[str] = pydantic.Field(alias="exp_year", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerCustomerSourceUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    owner: typing.Optional[_SerializerCustomerSourceUpdateBodyOwner] = pydantic.Field(
        alias="owner", default=None
    )
