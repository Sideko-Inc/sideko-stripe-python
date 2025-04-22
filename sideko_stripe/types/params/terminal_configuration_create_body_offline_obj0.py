import pydantic
import typing_extensions


class TerminalConfigurationCreateBodyOfflineObj0(typing_extensions.TypedDict):
    """
    TerminalConfigurationCreateBodyOfflineObj0
    """

    enabled: typing_extensions.Required[bool]


class _SerializerTerminalConfigurationCreateBodyOfflineObj0(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationCreateBodyOfflineObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
