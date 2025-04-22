import pydantic
import typing_extensions


class TerminalConfigurationUpdateBodyRebootWindowObj0(typing_extensions.TypedDict):
    """
    TerminalConfigurationUpdateBodyRebootWindowObj0
    """

    end_hour: typing_extensions.Required[int]

    start_hour: typing_extensions.Required[int]


class _SerializerTerminalConfigurationUpdateBodyRebootWindowObj0(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationUpdateBodyRebootWindowObj0 handling case conversions
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
