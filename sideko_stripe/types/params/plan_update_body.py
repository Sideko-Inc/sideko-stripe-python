import pydantic
import typing
import typing_extensions

from .plan_update_body_metadata_obj0 import (
    PlanUpdateBodyMetadataObj0,
    _SerializerPlanUpdateBodyMetadataObj0,
)


class PlanUpdateBody(typing_extensions.TypedDict, total=False):
    """
    PlanUpdateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Whether the plan is currently available for new subscriptions.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[PlanUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    nickname: typing_extensions.NotRequired[str]
    """
    A brief description of the plan, hidden from customers.
    """

    product: typing_extensions.NotRequired[str]
    """
    The product the plan belongs to. This cannot be changed once it has been used in a subscription or subscription schedule.
    """

    trial_period_days: typing_extensions.NotRequired[int]
    """
    Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan).
    """


class _SerializerPlanUpdateBody(pydantic.BaseModel):
    """
    Serializer for PlanUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerPlanUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    nickname: typing.Optional[str] = pydantic.Field(alias="nickname", default=None)
    product: typing.Optional[str] = pydantic.Field(alias="product", default=None)
    trial_period_days: typing.Optional[int] = pydantic.Field(
        alias="trial_period_days", default=None
    )
