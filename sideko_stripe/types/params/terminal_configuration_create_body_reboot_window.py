import pydantic
import typing_extensions


class TerminalConfigurationCreateBodyRebootWindow(typing_extensions.TypedDict):
    """
    Reboot time settings for readers that support customized reboot time configuration.
    """

    end_hour: typing_extensions.Required[int]

    start_hour: typing_extensions.Required[int]


class _SerializerTerminalConfigurationCreateBodyRebootWindow(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationCreateBodyRebootWindow handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_hour: int = pydantic.Field(
        alias="end_hour",
    )
    start_hour: int = pydantic.Field(
        alias="start_hour",
    )
