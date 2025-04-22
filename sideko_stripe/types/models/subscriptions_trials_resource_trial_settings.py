import pydantic

from .subscriptions_trials_resource_end_behavior import (
    SubscriptionsTrialsResourceEndBehavior,
)


class SubscriptionsTrialsResourceTrialSettings(pydantic.BaseModel):
    """
    Configures how this subscription behaves during the trial period.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    end_behavior: SubscriptionsTrialsResourceEndBehavior = pydantic.Field(
        alias="end_behavior",
    )
    """
    Defines how a subscription behaves when a free trial ends.
    """
