import pydantic
import typing


class TerminalConfigurationConfigurationResourceCurrencySpecificConfig(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fixed_amounts: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="fixed_amounts", default=None
    )
    """
    Fixed amounts displayed when collecting a tip
    """
    percentages: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="percentages", default=None
    )
    """
    Percentages displayed when collecting a tip
    """
    smart_tip_threshold: typing.Optional[int] = pydantic.Field(
        alias="smart_tip_threshold", default=None
    )
    """
    Below this amount, fixed amounts will be displayed; above it, percentages will be displayed
    """
