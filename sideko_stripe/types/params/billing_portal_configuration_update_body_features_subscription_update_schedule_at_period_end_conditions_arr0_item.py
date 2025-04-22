import pydantic
import typing_extensions


class BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsArr0Item(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsArr0Item
    """

    type_: typing_extensions.Required[
        typing_extensions.Literal["decreasing_item_amount", "shortening_interval"]
    ]


class _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsArr0Item(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsArr0Item handling case conversions
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
