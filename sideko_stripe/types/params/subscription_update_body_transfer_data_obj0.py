import pydantic
import typing
import typing_extensions


class SubscriptionUpdateBodyTransferDataObj0(typing_extensions.TypedDict):
    """
    SubscriptionUpdateBodyTransferDataObj0
    """

    amount_percent: typing_extensions.NotRequired[float]

    destination: typing_extensions.Required[str]


class _SerializerSubscriptionUpdateBodyTransferDataObj0(pydantic.BaseModel):
    """
    Serializer for SubscriptionUpdateBodyTransferDataObj0 handling case conversions
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
