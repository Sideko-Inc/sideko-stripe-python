import pydantic
import typing_extensions


class BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsItem(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsItem
    """

    type_: typing_extensions.Required[
        typing_extensions.Literal["decreasing_item_amount", "shortening_interval"]
    ]


class _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsItem(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal[
        "decreasing_item_amount", "shortening_interval"
    ] = pydantic.Field(
        alias="type",
    )
