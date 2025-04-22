import pydantic
import typing
import typing_extensions


class PlanCreateBodyProductObj0Metadata(typing_extensions.TypedDict, total=False):
    """
    PlanCreateBodyProductObj0Metadata
    """


class _SerializerPlanCreateBodyProductObj0Metadata(pydantic.BaseModel):
    """
    Serializer for PlanCreateBodyProductObj0Metadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
