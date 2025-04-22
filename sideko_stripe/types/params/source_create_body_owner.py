import pydantic
import typing
import typing_extensions

from .source_create_body_owner_address import (
    SourceCreateBodyOwnerAddress,
    _SerializerSourceCreateBodyOwnerAddress,
)


class SourceCreateBodyOwner(typing_extensions.TypedDict):
    """
    Information about the owner of the payment instrument that may be used or required by particular source types.
    """

    address: typing_extensions.NotRequired[SourceCreateBodyOwnerAddress]

    email: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]


class _SerializerSourceCreateBodyOwner(pydantic.BaseModel):
    """
    Serializer for SourceCreateBodyOwner handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[_SerializerSourceCreateBodyOwnerAddress] = pydantic.Field(
        alias="address", default=None
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
