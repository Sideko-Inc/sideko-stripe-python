import pydantic
import typing
import typing_extensions

from .billing_portal_configuration_create_body_features_subscription_update_schedule_at_period_end_conditions_item import (
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsItem,
    _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsItem,
)


class BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd
    """

    conditions: typing_extensions.NotRequired[
        typing.List[
            BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsItem
        ]
    ]


class _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    conditions: typing.Optional[
        typing.List[
            _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsItem
        ]
    ] = pydantic.Field(alias="conditions", default=None)
