import pydantic
import typing
import typing_extensions

from .billing_alert_create_body_usage_threshold_filters_item import (
    BillingAlertCreateBodyUsageThresholdFiltersItem,
    _SerializerBillingAlertCreateBodyUsageThresholdFiltersItem,
)


class BillingAlertCreateBodyUsageThreshold(typing_extensions.TypedDict):
    """
    The configuration of the usage threshold.
    """

    filters: typing_extensions.NotRequired[
        typing.List[BillingAlertCreateBodyUsageThresholdFiltersItem]
    ]

    gte: typing_extensions.Required[int]

    meter: typing_extensions.NotRequired[str]

    recurrence: typing_extensions.Required[typing_extensions.Literal["one_time"]]


class _SerializerBillingAlertCreateBodyUsageThreshold(pydantic.BaseModel):
    """
    Serializer for BillingAlertCreateBodyUsageThreshold handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    filters: typing.Optional[
        typing.List[_SerializerBillingAlertCreateBodyUsageThresholdFiltersItem]
    ] = pydantic.Field(alias="filters", default=None)
    gte: int = pydantic.Field(
        alias="gte",
    )
    meter: typing.Optional[str] = pydantic.Field(alias="meter", default=None)
    recurrence: typing_extensions.Literal["one_time"] = pydantic.Field(
        alias="recurrence",
    )
