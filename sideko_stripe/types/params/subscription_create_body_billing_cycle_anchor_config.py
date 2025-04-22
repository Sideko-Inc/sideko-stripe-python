import pydantic
import typing
import typing_extensions


class SubscriptionCreateBodyBillingCycleAnchorConfig(typing_extensions.TypedDict):
    """
    Mutually exclusive with billing_cycle_anchor and only valid with monthly and yearly price intervals. When provided, the billing_cycle_anchor is set to the next occurence of the day_of_month at the hour, minute, and second UTC.
    """

    day_of_month: typing_extensions.Required[int]

    hour: typing_extensions.NotRequired[int]

    minute: typing_extensions.NotRequired[int]

    month: typing_extensions.NotRequired[int]

    second: typing_extensions.NotRequired[int]


class _SerializerSubscriptionCreateBodyBillingCycleAnchorConfig(pydantic.BaseModel):
    """
    Serializer for SubscriptionCreateBodyBillingCycleAnchorConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    day_of_month: int = pydantic.Field(
        alias="day_of_month",
    )
    hour: typing.Optional[int] = pydantic.Field(alias="hour", default=None)
    minute: typing.Optional[int] = pydantic.Field(alias="minute", default=None)
    month: typing.Optional[int] = pydantic.Field(alias="month", default=None)
    second: typing.Optional[int] = pydantic.Field(alias="second", default=None)
