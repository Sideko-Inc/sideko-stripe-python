import pydantic
import typing
import typing_extensions

from .terminal_configuration_create_body_wifi_obj0_enterprise_eap_peap import (
    TerminalConfigurationCreateBodyWifiObj0EnterpriseEapPeap,
    _SerializerTerminalConfigurationCreateBodyWifiObj0EnterpriseEapPeap,
)
from .terminal_configuration_create_body_wifi_obj0_enterprise_eap_tls import (
    TerminalConfigurationCreateBodyWifiObj0EnterpriseEapTls,
    _SerializerTerminalConfigurationCreateBodyWifiObj0EnterpriseEapTls,
)
from .terminal_configuration_create_body_wifi_obj0_personal_psk import (
    TerminalConfigurationCreateBodyWifiObj0PersonalPsk,
    _SerializerTerminalConfigurationCreateBodyWifiObj0PersonalPsk,
)


class TerminalConfigurationCreateBodyWifiObj0(typing_extensions.TypedDict):
    """
    TerminalConfigurationCreateBodyWifiObj0
    """

    enterprise_eap_peap: typing_extensions.NotRequired[
        TerminalConfigurationCreateBodyWifiObj0EnterpriseEapPeap
    ]

    enterprise_eap_tls: typing_extensions.NotRequired[
        TerminalConfigurationCreateBodyWifiObj0EnterpriseEapTls
    ]

    personal_psk: typing_extensions.NotRequired[
        TerminalConfigurationCreateBodyWifiObj0PersonalPsk
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal[
            "enterprise_eap_peap", "enterprise_eap_tls", "personal_psk"
        ]
    ]


class _SerializerTerminalConfigurationCreateBodyWifiObj0(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationCreateBodyWifiObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enterprise_eap_peap: typing.Optional[
        _SerializerTerminalConfigurationCreateBodyWifiObj0EnterpriseEapPeap
    ] = pydantic.Field(alias="enterprise_eap_peap", default=None)
    enterprise_eap_tls: typing.Optional[
        _SerializerTerminalConfigurationCreateBodyWifiObj0EnterpriseEapTls
    ] = pydantic.Field(alias="enterprise_eap_tls", default=None)
    personal_psk: typing.Optional[
        _SerializerTerminalConfigurationCreateBodyWifiObj0PersonalPsk
    ] = pydantic.Field(alias="personal_psk", default=None)
    type_: typing_extensions.Literal[
        "enterprise_eap_peap", "enterprise_eap_tls", "personal_psk"
    ] = pydantic.Field(
        alias="type",
    )
