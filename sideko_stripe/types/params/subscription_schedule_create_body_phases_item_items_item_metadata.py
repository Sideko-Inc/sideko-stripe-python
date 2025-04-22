import pydantic
import typing
import typing_extensions


class SubscriptionScheduleCreateBodyPhasesItemItemsItemMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    SubscriptionScheduleCreateBodyPhasesItemItemsItemMetadata
    """


class _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemMetadata(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItemItemsItemMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
