import pydantic
import typing
import typing_extensions

from .terminal_location import TerminalLocation
from .terminal_reader_metadata import TerminalReaderMetadata

if typing_extensions.TYPE_CHECKING:
    from .terminal_reader_reader_resource_reader_action import (
        TerminalReaderReaderResourceReaderAction,
    )


class TerminalReader(pydantic.BaseModel):
    """
    A Reader represents a physical device for accepting payment details.

    Related guide: [Connecting to a reader](https://stripe.com/docs/terminal/payments/connect-reader)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    action: typing.Optional["TerminalReaderReaderResourceReaderAction"] = (
        pydantic.Field(alias="action", default=None)
    )
    """
    Represents an action performed by the reader
    """
    device_sw_version: typing.Optional[str] = pydantic.Field(
        alias="device_sw_version", default=None
    )
    """
    The current software version of the reader.
    """
    device_type: typing_extensions.Literal[
        "bbpos_chipper2x",
        "bbpos_wisepad3",
        "bbpos_wisepos_e",
        "mobile_phone_reader",
        "simulated_wisepos_e",
        "stripe_m2",
        "stripe_s700",
        "verifone_P400",
    ] = pydantic.Field(
        alias="device_type",
    )
    """
    Type of reader, one of `bbpos_wisepad3`, `stripe_m2`, `stripe_s700`, `bbpos_chipper2x`, `bbpos_wisepos_e`, `verifone_P400`, `simulated_wisepos_e`, or `mobile_phone_reader`.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    """
    The local IP address of the reader.
    """
    label: str = pydantic.Field(
        alias="label",
    )
    """
    Custom label given to the reader for easier identification.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    location: typing.Optional[typing.Union[str, TerminalLocation]] = pydantic.Field(
        alias="location", default=None
    )
    """
    The location identifier of the reader.
    """
    metadata: TerminalReaderMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["terminal.reader"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    serial_number: str = pydantic.Field(
        alias="serial_number",
    )
    """
    Serial number of the reader.
    """
    status: typing.Optional[typing_extensions.Literal["offline", "online"]] = (
        pydantic.Field(alias="status", default=None)
    )
    """
    The networking status of the reader. We do not recommend using this field in flows that may block taking payments.
    """
