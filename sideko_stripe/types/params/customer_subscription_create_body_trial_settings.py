import pydantic
import typing_extensions

from .customer_subscription_create_body_trial_settings_end_behavior import (
    CustomerSubscriptionCreateBodyTrialSettingsEndBehavior,
    _SerializerCustomerSubscriptionCreateBodyTrialSettingsEndBehavior,
)


class CustomerSubscriptionCreateBodyTrialSettings(typing_extensions.TypedDict):
    """
    Settings related to subscription trials.
    """

    end_behavior: typing_extensions.Required[
        CustomerSubscriptionCreateBodyTrialSettingsEndBehavior
    ]


class _SerializerCustomerSubscriptionCreateBodyTrialSettings(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionCreateBodyTrialSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_behavior: _SerializerCustomerSubscriptionCreateBodyTrialSettingsEndBehavior = (
        pydantic.Field(
            alias="end_behavior",
        )
    )
