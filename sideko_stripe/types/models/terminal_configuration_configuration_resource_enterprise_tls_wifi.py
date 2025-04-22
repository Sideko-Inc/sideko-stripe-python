import pydantic
import typing


class TerminalConfigurationConfigurationResourceEnterpriseTlsWifi(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ca_certificate_file: typing.Optional[str] = pydantic.Field(
        alias="ca_certificate_file", default=None
    )
    """
    A File ID representing a PEM file containing the server certificate
    """
    client_certificate_file: str = pydantic.Field(
        alias="client_certificate_file",
    )
    """
    A File ID representing a PEM file containing the client certificate
    """
    private_key_file: str = pydantic.Field(
        alias="private_key_file",
    )
    """
    A File ID representing a PEM file containing the client RSA private key
    """
    private_key_file_password: typing.Optional[str] = pydantic.Field(
        alias="private_key_file_password", default=None
    )
    """
    Password for the private key file
    """
    ssid: str = pydantic.Field(
        alias="ssid",
    )
    """
    Name of the WiFi network
    """
