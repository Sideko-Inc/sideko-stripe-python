import pydantic
import typing
import typing_extensions


class SubscriptionScheduleUpdateBodyPhasesItemItemsItemMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    SubscriptionScheduleUpdateBodyPhasesItemItemsItemMetadata
    """


class _SerializerSubscriptionScheduleUpdateBodyPhasesItemItemsItemMetadata(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleUpdateBodyPhasesItemItemsItemMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
