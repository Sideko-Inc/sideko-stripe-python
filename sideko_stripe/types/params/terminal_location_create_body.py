import pydantic
import typing
import typing_extensions

from .terminal_location_create_body_address import (
    TerminalLocationCreateBodyAddress,
    _SerializerTerminalLocationCreateBodyAddress,
)
from .terminal_location_create_body_metadata_obj0 import (
    TerminalLocationCreateBodyMetadataObj0,
    _SerializerTerminalLocationCreateBodyMetadataObj0,
)


class TerminalLocationCreateBody(typing_extensions.TypedDict, total=False):
    """
    TerminalLocationCreateBody
    """

    address: typing_extensions.Required[TerminalLocationCreateBodyAddress]
    """
    The full address of the location.
    """

    configuration_overrides: typing_extensions.NotRequired[str]
    """
    The ID of a configuration that will be used to customize all readers in this location.
    """

    display_name: typing_extensions.Required[str]
    """
    A name for the location. Maximum length is 1000 characters.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[TerminalLocationCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerTerminalLocationCreateBody(pydantic.BaseModel):
    """
    Serializer for TerminalLocationCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    address: _SerializerTerminalLocationCreateBodyAddress = pydantic.Field(
        alias="address",
    )
    configuration_overrides: typing.Optional[str] = pydantic.Field(
        alias="configuration_overrides", default=None
    )
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerTerminalLocationCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
