import pydantic
import typing
import typing_extensions


class IssuingDisputeListCreatedObj0(typing_extensions.TypedDict):
    """
    IssuingDisputeListCreatedObj0
    """

    gt: typing_extensions.NotRequired[int]

    gte: typing_extensions.NotRequired[int]

    lt: typing_extensions.NotRequired[int]

    lte: typing_extensions.NotRequired[int]


class _SerializerIssuingDisputeListCreatedObj0(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeListCreatedObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    gt: typing.Optional[int] = pydantic.Field(alias="gt", default=None)
    gte: typing.Optional[int] = pydantic.Field(alias="gte", default=None)
    lt: typing.Optional[int] = pydantic.Field(alias="lt", default=None)
    lte: typing.Optional[int] = pydantic.Field(alias="lte", default=None)
