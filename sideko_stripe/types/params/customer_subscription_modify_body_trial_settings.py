import pydantic
import typing_extensions

from .customer_subscription_modify_body_trial_settings_end_behavior import (
    CustomerSubscriptionModifyBodyTrialSettingsEndBehavior,
    _SerializerCustomerSubscriptionModifyBodyTrialSettingsEndBehavior,
)


class CustomerSubscriptionModifyBodyTrialSettings(typing_extensions.TypedDict):
    """
    Settings related to subscription trials.
    """

    end_behavior: typing_extensions.Required[
        CustomerSubscriptionModifyBodyTrialSettingsEndBehavior
    ]


class _SerializerCustomerSubscriptionModifyBodyTrialSettings(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionModifyBodyTrialSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_behavior: _SerializerCustomerSubscriptionModifyBodyTrialSettingsEndBehavior = (
        pydantic.Field(
            alias="end_behavior",
        )
    )
