import pydantic
import typing_extensions


class PlanCreateBodyTransformUsage(typing_extensions.TypedDict):
    """
    Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
    """

    divide_by: typing_extensions.Required[int]

    round: typing_extensions.Required[typing_extensions.Literal["down", "up"]]


class _SerializerPlanCreateBodyTransformUsage(pydantic.BaseModel):
    """
    Serializer for PlanCreateBodyTransformUsage handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    divide_by: int = pydantic.Field(
        alias="divide_by",
    )
    round: typing_extensions.Literal["down", "up"] = pydantic.Field(
        alias="round",
    )
