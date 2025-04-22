import pydantic
import typing
import typing_extensions

from .terminal_configuration_update_body_wifi_obj0_enterprise_eap_peap import (
    TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapPeap,
    _SerializerTerminalConfigurationUpdateBodyWifiObj0EnterpriseEapPeap,
)
from .terminal_configuration_update_body_wifi_obj0_enterprise_eap_tls import (
    TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapTls,
    _SerializerTerminalConfigurationUpdateBodyWifiObj0EnterpriseEapTls,
)
from .terminal_configuration_update_body_wifi_obj0_personal_psk import (
    TerminalConfigurationUpdateBodyWifiObj0PersonalPsk,
    _SerializerTerminalConfigurationUpdateBodyWifiObj0PersonalPsk,
)


class TerminalConfigurationUpdateBodyWifiObj0(typing_extensions.TypedDict):
    """
    TerminalConfigurationUpdateBodyWifiObj0
    """

    enterprise_eap_peap: typing_extensions.NotRequired[
        TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapPeap
    ]

    enterprise_eap_tls: typing_extensions.NotRequired[
        TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapTls
    ]

    personal_psk: typing_extensions.NotRequired[
        TerminalConfigurationUpdateBodyWifiObj0PersonalPsk
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal[
            "enterprise_eap_peap", "enterprise_eap_tls", "personal_psk"
        ]
    ]


class _SerializerTerminalConfigurationUpdateBodyWifiObj0(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationUpdateBodyWifiObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enterprise_eap_peap: typing.Optional[
        _SerializerTerminalConfigurationUpdateBodyWifiObj0EnterpriseEapPeap
    ] = pydantic.Field(alias="enterprise_eap_peap", default=None)
    enterprise_eap_tls: typing.Optional[
        _SerializerTerminalConfigurationUpdateBodyWifiObj0EnterpriseEapTls
    ] = pydantic.Field(alias="enterprise_eap_tls", default=None)
    personal_psk: typing.Optional[
        _SerializerTerminalConfigurationUpdateBodyWifiObj0PersonalPsk
    ] = pydantic.Field(alias="personal_psk", default=None)
    type_: typing_extensions.Literal[
        "enterprise_eap_peap", "enterprise_eap_tls", "personal_psk"
    ] = pydantic.Field(
        alias="type",
    )
