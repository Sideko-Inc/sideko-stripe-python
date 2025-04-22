import pydantic
import typing
import typing_extensions


class TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapPeap(
    typing_extensions.TypedDict
):
    """
    TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapPeap
    """

    ca_certificate_file: typing_extensions.NotRequired[str]

    password: typing_extensions.Required[str]

    ssid: typing_extensions.Required[str]

    username: typing_extensions.Required[str]


class _SerializerTerminalConfigurationUpdateBodyWifiObj0EnterpriseEapPeap(
    pydantic.BaseModel
):
    """
    Serializer for TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapPeap handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ca_certificate_file: typing.Optional[str] = pydantic.Field(
        alias="ca_certificate_file", default=None
    )
    password: str = pydantic.Field(
        alias="password",
    )
    ssid: str = pydantic.Field(
        alias="ssid",
    )
    username: str = pydantic.Field(
        alias="username",
    )
