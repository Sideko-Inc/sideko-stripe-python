import pydantic
import typing
import typing_extensions

from .billing_alert_create_body_usage_threshold import (
    BillingAlertCreateBodyUsageThreshold,
    _SerializerBillingAlertCreateBodyUsageThreshold,
)


class BillingAlertCreateBody(typing_extensions.TypedDict, total=False):
    """
    BillingAlertCreateBody
    """

    alert_type: typing_extensions.Required[typing_extensions.Literal["usage_threshold"]]
    """
    The type of alert to create.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    title: typing_extensions.Required[str]
    """
    The title of the alert.
    """

    usage_threshold: typing_extensions.NotRequired[BillingAlertCreateBodyUsageThreshold]
    """
    The configuration of the usage threshold.
    """


class _SerializerBillingAlertCreateBody(pydantic.BaseModel):
    """
    Serializer for BillingAlertCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    alert_type: typing_extensions.Literal["usage_threshold"] = pydantic.Field(
        alias="alert_type",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    title: str = pydantic.Field(
        alias="title",
    )
    usage_threshold: typing.Optional[
        _SerializerBillingAlertCreateBodyUsageThreshold
    ] = pydantic.Field(alias="usage_threshold", default=None)
