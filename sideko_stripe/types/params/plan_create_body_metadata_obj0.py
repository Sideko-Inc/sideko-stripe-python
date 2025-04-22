import pydantic
import typing
import typing_extensions


class PlanCreateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    PlanCreateBodyMetadataObj0
    """


class _SerializerPlanCreateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for PlanCreateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
