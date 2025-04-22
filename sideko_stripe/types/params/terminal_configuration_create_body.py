import pydantic
import typing
import typing_extensions

from .terminal_configuration_create_body_bbpos_wisepos_e import (
    TerminalConfigurationCreateBodyBbposWiseposE,
    _SerializerTerminalConfigurationCreateBodyBbposWiseposE,
)
from .terminal_configuration_create_body_offline_obj0 import (
    TerminalConfigurationCreateBodyOfflineObj0,
    _SerializerTerminalConfigurationCreateBodyOfflineObj0,
)
from .terminal_configuration_create_body_reboot_window import (
    TerminalConfigurationCreateBodyRebootWindow,
    _SerializerTerminalConfigurationCreateBodyRebootWindow,
)
from .terminal_configuration_create_body_stripe_s700 import (
    TerminalConfigurationCreateBodyStripeS700,
    _SerializerTerminalConfigurationCreateBodyStripeS700,
)
from .terminal_configuration_create_body_tipping_obj0 import (
    TerminalConfigurationCreateBodyTippingObj0,
    _SerializerTerminalConfigurationCreateBodyTippingObj0,
)
from .terminal_configuration_create_body_verifone_p400 import (
    TerminalConfigurationCreateBodyVerifoneP400,
    _SerializerTerminalConfigurationCreateBodyVerifoneP400,
)
from .terminal_configuration_create_body_wifi_obj0 import (
    TerminalConfigurationCreateBodyWifiObj0,
    _SerializerTerminalConfigurationCreateBodyWifiObj0,
)


class TerminalConfigurationCreateBody(typing_extensions.TypedDict, total=False):
    """
    TerminalConfigurationCreateBody
    """

    bbpos_wisepos_e: typing_extensions.NotRequired[
        TerminalConfigurationCreateBodyBbposWiseposE
    ]
    """
    An object containing device type specific settings for BBPOS WisePOS E readers
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    name: typing_extensions.NotRequired[str]
    """
    Name of the configuration
    """

    offline: typing_extensions.NotRequired[
        typing.Union[TerminalConfigurationCreateBodyOfflineObj0, str]
    ]
    """
    Configurations for collecting transactions offline.
    """

    reboot_window: typing_extensions.NotRequired[
        TerminalConfigurationCreateBodyRebootWindow
    ]
    """
    Reboot time settings for readers that support customized reboot time configuration.
    """

    stripe_s700: typing_extensions.NotRequired[
        TerminalConfigurationCreateBodyStripeS700
    ]
    """
    An object containing device type specific settings for Stripe S700 readers
    """

    tipping: typing_extensions.NotRequired[
        typing.Union[TerminalConfigurationCreateBodyTippingObj0, str]
    ]
    """
    Tipping configurations for readers supporting on-reader tips
    """

    verifone_p400: typing_extensions.NotRequired[
        TerminalConfigurationCreateBodyVerifoneP400
    ]
    """
    An object containing device type specific settings for Verifone P400 readers
    """

    wifi: typing_extensions.NotRequired[
        typing.Union[TerminalConfigurationCreateBodyWifiObj0, str]
    ]
    """
    Configurations for connecting to a WiFi network.
    """


class _SerializerTerminalConfigurationCreateBody(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    bbpos_wisepos_e: typing.Optional[
        _SerializerTerminalConfigurationCreateBodyBbposWiseposE
    ] = pydantic.Field(alias="bbpos_wisepos_e", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    offline: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationCreateBodyOfflineObj0, str]
    ] = pydantic.Field(alias="offline", default=None)
    reboot_window: typing.Optional[
        _SerializerTerminalConfigurationCreateBodyRebootWindow
    ] = pydantic.Field(alias="reboot_window", default=None)
    stripe_s700: typing.Optional[
        _SerializerTerminalConfigurationCreateBodyStripeS700
    ] = pydantic.Field(alias="stripe_s700", default=None)
    tipping: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationCreateBodyTippingObj0, str]
    ] = pydantic.Field(alias="tipping", default=None)
    verifone_p400: typing.Optional[
        _SerializerTerminalConfigurationCreateBodyVerifoneP400
    ] = pydantic.Field(alias="verifone_p400", default=None)
    wifi: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationCreateBodyWifiObj0, str]
    ] = pydantic.Field(alias="wifi", default=None)
