import pydantic
import typing


class TerminalConfigurationConfigurationResourceOfflineConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    """
    Determines whether to allow transactions to be collected while reader is offline. Defaults to false.
    """
