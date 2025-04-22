import pydantic
import typing
import typing_extensions


class SubscriptionScheduleCreateBodyPhasesItemMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    SubscriptionScheduleCreateBodyPhasesItemMetadata
    """


class _SerializerSubscriptionScheduleCreateBodyPhasesItemMetadata(pydantic.BaseModel):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItemMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
