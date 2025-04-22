import pydantic
import typing
import typing_extensions

from .terminal_configuration_configuration_resource_enterprise_peap_wifi import (
    TerminalConfigurationConfigurationResourceEnterprisePeapWifi,
)
from .terminal_configuration_configuration_resource_enterprise_tls_wifi import (
    TerminalConfigurationConfigurationResourceEnterpriseTlsWifi,
)
from .terminal_configuration_configuration_resource_personal_psk_wifi import (
    TerminalConfigurationConfigurationResourcePersonalPskWifi,
)


class TerminalConfigurationConfigurationResourceWifiConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enterprise_eap_peap: typing.Optional[
        TerminalConfigurationConfigurationResourceEnterprisePeapWifi
    ] = pydantic.Field(alias="enterprise_eap_peap", default=None)
    enterprise_eap_tls: typing.Optional[
        TerminalConfigurationConfigurationResourceEnterpriseTlsWifi
    ] = pydantic.Field(alias="enterprise_eap_tls", default=None)
    personal_psk: typing.Optional[
        TerminalConfigurationConfigurationResourcePersonalPskWifi
    ] = pydantic.Field(alias="personal_psk", default=None)
    type_: typing_extensions.Literal[
        "enterprise_eap_peap", "enterprise_eap_tls", "personal_psk"
    ] = pydantic.Field(
        alias="type",
    )
    """
    Security type of the WiFi network. The hash with the corresponding name contains the credentials for this security type.
    """
