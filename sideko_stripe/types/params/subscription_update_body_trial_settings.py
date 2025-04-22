import pydantic
import typing_extensions

from .subscription_update_body_trial_settings_end_behavior import (
    SubscriptionUpdateBodyTrialSettingsEndBehavior,
    _SerializerSubscriptionUpdateBodyTrialSettingsEndBehavior,
)


class SubscriptionUpdateBodyTrialSettings(typing_extensions.TypedDict):
    """
    Settings related to subscription trials.
    """

    end_behavior: typing_extensions.Required[
        SubscriptionUpdateBodyTrialSettingsEndBehavior
    ]


class _SerializerSubscriptionUpdateBodyTrialSettings(pydantic.BaseModel):
    """
    Serializer for SubscriptionUpdateBodyTrialSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_behavior: _SerializerSubscriptionUpdateBodyTrialSettingsEndBehavior = (
        pydantic.Field(
            alias="end_behavior",
        )
    )
