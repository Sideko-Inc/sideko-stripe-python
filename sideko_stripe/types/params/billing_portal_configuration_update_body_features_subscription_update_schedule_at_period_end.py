import pydantic
import typing
import typing_extensions

from .billing_portal_configuration_update_body_features_subscription_update_schedule_at_period_end_conditions_arr0_item import (
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsArr0Item,
    _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsArr0Item,
)


class BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd
    """

    conditions: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsArr0Item
            ],
            str,
        ]
    ]


class _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    conditions: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEndConditionsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="conditions", default=None)
