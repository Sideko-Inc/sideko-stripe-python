import pydantic
import typing
import typing_extensions


class TerminalConfigurationCreateBodyTippingObj0Sgd(typing_extensions.TypedDict):
    """
    TerminalConfigurationCreateBodyTippingObj0Sgd
    """

    fixed_amounts: typing_extensions.NotRequired[typing.List[int]]

    percentages: typing_extensions.NotRequired[typing.List[int]]

    smart_tip_threshold: typing_extensions.NotRequired[int]


class _SerializerTerminalConfigurationCreateBodyTippingObj0Sgd(pydantic.BaseModel):
    """
    Serializer for TerminalConfigurationCreateBodyTippingObj0Sgd handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fixed_amounts: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="fixed_amounts", default=None
    )
    percentages: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="percentages", default=None
    )
    smart_tip_threshold: typing.Optional[int] = pydantic.Field(
        alias="smart_tip_threshold", default=None
    )
