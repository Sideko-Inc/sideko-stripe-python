import pydantic
import typing_extensions


class TerminalConfigurationUpdateBodyWifiObj0PersonalPsk(typing_extensions.TypedDict):
    """
    TerminalConfigurationUpdateBodyWifiObj0PersonalPsk
    """

    password: typing_extensions.Required[str]

    ssid: typing_extensions.Required[str]


class _SerializerTerminalConfigurationUpdateBodyWifiObj0PersonalPsk(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationUpdateBodyWifiObj0PersonalPsk handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    password: str = pydantic.Field(
        alias="password",
    )
    ssid: str = pydantic.Field(
        alias="ssid",
    )
