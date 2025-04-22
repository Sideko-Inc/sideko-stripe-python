import pydantic


class TerminalConfigurationConfigurationResourcePersonalPskWifi(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

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
