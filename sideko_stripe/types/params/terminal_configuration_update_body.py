import pydantic
import typing
import typing_extensions

from .terminal_configuration_update_body_bbpos_wisepos_e_obj0 import (
    TerminalConfigurationUpdateBodyBbposWiseposEObj0,
    _SerializerTerminalConfigurationUpdateBodyBbposWiseposEObj0,
)
from .terminal_configuration_update_body_offline_obj0 import (
    TerminalConfigurationUpdateBodyOfflineObj0,
    _SerializerTerminalConfigurationUpdateBodyOfflineObj0,
)
from .terminal_configuration_update_body_reboot_window_obj0 import (
    TerminalConfigurationUpdateBodyRebootWindowObj0,
    _SerializerTerminalConfigurationUpdateBodyRebootWindowObj0,
)
from .terminal_configuration_update_body_stripe_s700_obj0 import (
    TerminalConfigurationUpdateBodyStripeS700Obj0,
    _SerializerTerminalConfigurationUpdateBodyStripeS700Obj0,
)
from .terminal_configuration_update_body_tipping_obj0 import (
    TerminalConfigurationUpdateBodyTippingObj0,
    _SerializerTerminalConfigurationUpdateBodyTippingObj0,
)
from .terminal_configuration_update_body_verifone_p400_obj0 import (
    TerminalConfigurationUpdateBodyVerifoneP400Obj0,
    _SerializerTerminalConfigurationUpdateBodyVerifoneP400Obj0,
)
from .terminal_configuration_update_body_wifi_obj0 import (
    TerminalConfigurationUpdateBodyWifiObj0,
    _SerializerTerminalConfigurationUpdateBodyWifiObj0,
)


class TerminalConfigurationUpdateBody(typing_extensions.TypedDict, total=False):
    """
    TerminalConfigurationUpdateBody
    """

    bbpos_wisepos_e: typing_extensions.NotRequired[
        typing.Union[TerminalConfigurationUpdateBodyBbposWiseposEObj0, str]
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
        typing.Union[TerminalConfigurationUpdateBodyOfflineObj0, str]
    ]
    """
    Configurations for collecting transactions offline.
    """

    reboot_window: typing_extensions.NotRequired[
        typing.Union[TerminalConfigurationUpdateBodyRebootWindowObj0, str]
    ]
    """
    Reboot time settings for readers that support customized reboot time configuration.
    """

    stripe_s700: typing_extensions.NotRequired[
        typing.Union[TerminalConfigurationUpdateBodyStripeS700Obj0, str]
    ]
    """
    An object containing device type specific settings for Stripe S700 readers
    """

    tipping: typing_extensions.NotRequired[
        typing.Union[TerminalConfigurationUpdateBodyTippingObj0, str]
    ]
    """
    Tipping configurations for readers supporting on-reader tips
    """

    verifone_p400: typing_extensions.NotRequired[
        typing.Union[TerminalConfigurationUpdateBodyVerifoneP400Obj0, str]
    ]
    """
    An object containing device type specific settings for Verifone P400 readers
    """

    wifi: typing_extensions.NotRequired[
        typing.Union[TerminalConfigurationUpdateBodyWifiObj0, str]
    ]
    """
    Configurations for connecting to a WiFi network.
    """


class _SerializerTerminalConfigurationUpdateBody(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    bbpos_wisepos_e: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationUpdateBodyBbposWiseposEObj0, str]
    ] = pydantic.Field(alias="bbpos_wisepos_e", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    offline: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationUpdateBodyOfflineObj0, str]
    ] = pydantic.Field(alias="offline", default=None)
    reboot_window: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationUpdateBodyRebootWindowObj0, str]
    ] = pydantic.Field(alias="reboot_window", default=None)
    stripe_s700: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationUpdateBodyStripeS700Obj0, str]
    ] = pydantic.Field(alias="stripe_s700", default=None)
    tipping: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationUpdateBodyTippingObj0, str]
    ] = pydantic.Field(alias="tipping", default=None)
    verifone_p400: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationUpdateBodyVerifoneP400Obj0, str]
    ] = pydantic.Field(alias="verifone_p400", default=None)
    wifi: typing.Optional[
        typing.Union[_SerializerTerminalConfigurationUpdateBodyWifiObj0, str]
    ] = pydantic.Field(alias="wifi", default=None)
