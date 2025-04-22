import pydantic
import typing
import typing_extensions


class TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapTls(
    typing_extensions.TypedDict
):
    """
    TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapTls
    """

    ca_certificate_file: typing_extensions.NotRequired[str]

    client_certificate_file: typing_extensions.Required[str]

    private_key_file: typing_extensions.Required[str]

    private_key_file_password: typing_extensions.NotRequired[str]

    ssid: typing_extensions.Required[str]


class _SerializerTerminalConfigurationUpdateBodyWifiObj0EnterpriseEapTls(
    pydantic.BaseModel
):
    """
    Serializer for TerminalConfigurationUpdateBodyWifiObj0EnterpriseEapTls handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ca_certificate_file: typing.Optional[str] = pydantic.Field(
        alias="ca_certificate_file", default=None
    )
    client_certificate_file: str = pydantic.Field(
        alias="client_certificate_file",
    )
    private_key_file: str = pydantic.Field(
        alias="private_key_file",
    )
    private_key_file_password: typing.Optional[str] = pydantic.Field(
        alias="private_key_file_password", default=None
    )
    ssid: str = pydantic.Field(
        alias="ssid",
    )
