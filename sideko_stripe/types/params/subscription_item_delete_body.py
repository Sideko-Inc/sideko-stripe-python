import pydantic
import typing
import typing_extensions


class SubscriptionItemDeleteBody(typing_extensions.TypedDict, total=False):
    """
    SubscriptionItemDeleteBody
    """

    clear_usage: typing_extensions.NotRequired[bool]
    """
    Delete all usage for the given subscription item. Allowed only when the current plan's `usage_type` is `metered`.
    """

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    """

    proration_date: typing_extensions.NotRequired[int]
    """
    If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint.
    """


class _SerializerSubscriptionItemDeleteBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionItemDeleteBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    clear_usage: typing.Optional[bool] = pydantic.Field(
        alias="clear_usage", default=None
    )
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    proration_date: typing.Optional[int] = pydantic.Field(
        alias="proration_date", default=None
    )
