import pydantic
import typing
import typing_extensions

from .source_update_body_owner_address import (
    SourceUpdateBodyOwnerAddress,
    _SerializerSourceUpdateBodyOwnerAddress,
)


class SourceUpdateBodyOwner(typing_extensions.TypedDict):
    """
    Information about the owner of the payment instrument that may be used or required by particular source types.
    """

    address: typing_extensions.NotRequired[SourceUpdateBodyOwnerAddress]

    email: typing_extensions.NotRequired[str]

    name: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]


class _SerializerSourceUpdateBodyOwner(pydantic.BaseModel):
    """
    Serializer for SourceUpdateBodyOwner handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[_SerializerSourceUpdateBodyOwnerAddress] = pydantic.Field(
        alias="address", default=None
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
