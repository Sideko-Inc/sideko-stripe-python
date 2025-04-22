import pydantic
import typing
import typing_extensions

from .terminal_location_update_body_address import (
    TerminalLocationUpdateBodyAddress,
    _SerializerTerminalLocationUpdateBodyAddress,
)
from .terminal_location_update_body_metadata_obj0 import (
    TerminalLocationUpdateBodyMetadataObj0,
    _SerializerTerminalLocationUpdateBodyMetadataObj0,
)


class TerminalLocationUpdateBody(typing_extensions.TypedDict, total=False):
    """
    TerminalLocationUpdateBody
    """

    address: typing_extensions.NotRequired[TerminalLocationUpdateBodyAddress]
    """
    The full address of the location. You can't change the location's `country`. If you need to modify the `country` field, create a new `Location` object and re-register any existing readers to that location.
    """

    configuration_overrides: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The ID of a configuration that will be used to customize all readers in this location.
    """

    display_name: typing_extensions.NotRequired[str]
    """
    A name for the location.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[TerminalLocationUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerTerminalLocationUpdateBody(pydantic.BaseModel):
    """
    Serializer for TerminalLocationUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    address: typing.Optional[_SerializerTerminalLocationUpdateBodyAddress] = (
        pydantic.Field(alias="address", default=None)
    )
    configuration_overrides: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="configuration_overrides", default=None
    )
    display_name: typing.Optional[str] = pydantic.Field(
        alias="display_name", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerTerminalLocationUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
