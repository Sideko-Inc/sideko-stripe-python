import pydantic
import typing
import typing_extensions

from .address import Address
from .terminal_location_metadata import TerminalLocationMetadata


class TerminalLocation(pydantic.BaseModel):
    """
    A Location represents a grouping of readers.

    Related guide: [Fleet management](https://stripe.com/docs/terminal/fleet/locations)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: Address = pydantic.Field(
        alias="address",
    )
    configuration_overrides: typing.Optional[str] = pydantic.Field(
        alias="configuration_overrides", default=None
    )
    """
    The ID of a configuration that will be used to customize all readers in this location.
    """
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    """
    The display name of the location.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: TerminalLocationMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["terminal.location"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
