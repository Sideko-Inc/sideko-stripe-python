import pydantic
import typing


class TerminalConfigurationConfigurationResourceEnterprisePeapWifi(pydantic.BaseModel):
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
    password: str = pydantic.Field(
        alias="password",
    )
    """
    Password for connecting to the WiFi network
    """
    ssid: str = pydantic.Field(
        alias="ssid",
    )
    """
    Name of the WiFi network
    """
    username: str = pydantic.Field(
        alias="username",
    )
    """
    Username for connecting to the WiFi network
    """
