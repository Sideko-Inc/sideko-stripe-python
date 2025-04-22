import pydantic
import typing
import typing_extensions


class SubscriptionResumeBody(typing_extensions.TypedDict, total=False):
    """
    SubscriptionResumeBody
    """

    billing_cycle_anchor: typing_extensions.NotRequired[
        typing_extensions.Literal["now", "unchanged"]
    ]
    """
    The billing cycle anchor that applies when the subscription is resumed. Either `now` or `unchanged`. The default is `now`. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    """

    proration_date: typing_extensions.NotRequired[int]
    """
    If set, the proration will be calculated as though the subscription was resumed at the given time. This can be used to apply exactly the same proration that was previewed with [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint.
    """


class _SerializerSubscriptionResumeBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionResumeBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    billing_cycle_anchor: typing.Optional[
        typing_extensions.Literal["now", "unchanged"]
    ] = pydantic.Field(alias="billing_cycle_anchor", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    proration_date: typing.Optional[int] = pydantic.Field(
        alias="proration_date", default=None
    )
