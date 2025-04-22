import pydantic
import typing_extensions


class TerminalConfigurationUpdateBodyOfflineObj0(typing_extensions.TypedDict):
    """
    TerminalConfigurationUpdateBodyOfflineObj0
    """

    enabled: typing_extensions.Required[bool]


class _SerializerTerminalConfigurationUpdateBodyOfflineObj0(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationUpdateBodyOfflineObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
