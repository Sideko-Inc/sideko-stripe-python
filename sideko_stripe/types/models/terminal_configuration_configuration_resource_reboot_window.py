import pydantic


class TerminalConfigurationConfigurationResourceRebootWindow(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    end_hour: int = pydantic.Field(
        alias="end_hour",
    )
    """
    Integer between 0 to 23 that represents the end hour of the reboot time window. The value must be different than the start_hour.
    """
    start_hour: int = pydantic.Field(
        alias="start_hour",
    )
    """
    Integer between 0 to 23 that represents the start hour of the reboot time window.
    """
