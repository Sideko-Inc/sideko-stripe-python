import pydantic
import typing
import typing_extensions


class ForwardingRequestListCreated(typing_extensions.TypedDict):
    """
    Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.
    """

    gt: typing_extensions.NotRequired[int]

    gte: typing_extensions.NotRequired[int]

    lt: typing_extensions.NotRequired[int]

    lte: typing_extensions.NotRequired[int]


class _SerializerForwardingRequestListCreated(pydantic.BaseModel):
    """
    Serializer for ForwardingRequestListCreated handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    gt: typing.Optional[int] = pydantic.Field(alias="gt", default=None)
    gte: typing.Optional[int] = pydantic.Field(alias="gte", default=None)
    lt: typing.Optional[int] = pydantic.Field(alias="lt", default=None)
    lte: typing.Optional[int] = pydantic.Field(alias="lte", default=None)
