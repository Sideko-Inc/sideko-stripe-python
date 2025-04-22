import pydantic
import typing
import typing_extensions


class SubscriptionScheduleUpdateBodyDefaultSettingsTransferDataObj0(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleUpdateBodyDefaultSettingsTransferDataObj0
    """

    amount_percent: typing_extensions.NotRequired[float]

    destination: typing_extensions.Required[str]


class _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsTransferDataObj0(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleUpdateBodyDefaultSettingsTransferDataObj0 handling case conversions
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
