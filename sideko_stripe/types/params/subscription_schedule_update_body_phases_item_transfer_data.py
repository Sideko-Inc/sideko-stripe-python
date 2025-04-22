import pydantic
import typing
import typing_extensions


class SubscriptionScheduleUpdateBodyPhasesItemTransferData(typing_extensions.TypedDict):
    """
    SubscriptionScheduleUpdateBodyPhasesItemTransferData
    """

    amount_percent: typing_extensions.NotRequired[float]

    destination: typing_extensions.Required[str]


class _SerializerSubscriptionScheduleUpdateBodyPhasesItemTransferData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleUpdateBodyPhasesItemTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_percent: typing.Optional[float] = pydantic.Field(
        alias="amount_percent", default=None
    )
    destination: str = pydantic.Field(
        alias="destination",
    )
