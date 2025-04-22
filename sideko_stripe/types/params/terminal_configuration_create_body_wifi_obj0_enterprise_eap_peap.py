import pydantic
import typing
import typing_extensions


class TerminalConfigurationCreateBodyWifiObj0EnterpriseEapPeap(
    typing_extensions.TypedDict
):
    """
    TerminalConfigurationCreateBodyWifiObj0EnterpriseEapPeap
    """

    ca_certificate_file: typing_extensions.NotRequired[str]

    password: typing_extensions.Required[str]

    ssid: typing_extensions.Required[str]

    username: typing_extensions.Required[str]


class _SerializerTerminalConfigurationCreateBodyWifiObj0EnterpriseEapPeap(
    pydantic.BaseModel
):
    """
    Serializer for TerminalConfigurationCreateBodyWifiObj0EnterpriseEapPeap handling case conversions
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
