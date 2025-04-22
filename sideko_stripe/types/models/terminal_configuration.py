import pydantic
import typing
import typing_extensions

from .terminal_configuration_configuration_resource_offline_config import (
    TerminalConfigurationConfigurationResourceOfflineConfig,
)
from .terminal_configuration_configuration_resource_reboot_window import (
    TerminalConfigurationConfigurationResourceRebootWindow,
)
from .terminal_configuration_configuration_resource_tipping import (
    TerminalConfigurationConfigurationResourceTipping,
)
from .terminal_configuration_configuration_resource_wifi_config import (
    TerminalConfigurationConfigurationResourceWifiConfig,
)

if typing_extensions.TYPE_CHECKING:
    from .terminal_configuration_configuration_resource_device_type_specific_config import (
        TerminalConfigurationConfigurationResourceDeviceTypeSpecificConfig,
    )


class TerminalConfiguration(pydantic.BaseModel):
    """
    A Configurations object represents how features should be configured for terminal readers.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bbpos_wisepos_e: typing.Optional[
        "TerminalConfigurationConfigurationResourceDeviceTypeSpecificConfig"
    ] = pydantic.Field(alias="bbpos_wisepos_e", default=None)
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    is_account_default: typing.Optional[bool] = pydantic.Field(
        alias="is_account_default", default=None
    )
    """
    Whether this Configuration is the default for your account
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    String indicating the name of the Configuration object, set by the user
    """
    object: typing_extensions.Literal["terminal.configuration"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    offline: typing.Optional[
        TerminalConfigurationConfigurationResourceOfflineConfig
    ] = pydantic.Field(alias="offline", default=None)
    reboot_window: typing.Optional[
        TerminalConfigurationConfigurationResourceRebootWindow
    ] = pydantic.Field(alias="reboot_window", default=None)
    stripe_s700: typing.Optional[
        "TerminalConfigurationConfigurationResourceDeviceTypeSpecificConfig"
    ] = pydantic.Field(alias="stripe_s700", default=None)
    tipping: typing.Optional[TerminalConfigurationConfigurationResourceTipping] = (
        pydantic.Field(alias="tipping", default=None)
    )
    verifone_p400: typing.Optional[
        "TerminalConfigurationConfigurationResourceDeviceTypeSpecificConfig"
    ] = pydantic.Field(alias="verifone_p400", default=None)
    wifi: typing.Optional[TerminalConfigurationConfigurationResourceWifiConfig] = (
        pydantic.Field(alias="wifi", default=None)
    )
