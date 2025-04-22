import pydantic
import typing_extensions

from .subscription_create_body_trial_settings_end_behavior import (
    SubscriptionCreateBodyTrialSettingsEndBehavior,
    _SerializerSubscriptionCreateBodyTrialSettingsEndBehavior,
)


class SubscriptionCreateBodyTrialSettings(typing_extensions.TypedDict):
    """
    Settings related to subscription trials.
    """

    end_behavior: typing_extensions.Required[
        SubscriptionCreateBodyTrialSettingsEndBehavior
    ]


class _SerializerSubscriptionCreateBodyTrialSettings(pydantic.BaseModel):
    """
    Serializer for SubscriptionCreateBodyTrialSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_behavior: _SerializerSubscriptionCreateBodyTrialSettingsEndBehavior = (
        pydantic.Field(
            alias="end_behavior",
        )
    )
