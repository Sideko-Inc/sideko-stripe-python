import pydantic
import typing_extensions

from .checkout_session_create_body_subscription_data_trial_settings_end_behavior import (
    CheckoutSessionCreateBodySubscriptionDataTrialSettingsEndBehavior,
    _SerializerCheckoutSessionCreateBodySubscriptionDataTrialSettingsEndBehavior,
)


class CheckoutSessionCreateBodySubscriptionDataTrialSettings(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodySubscriptionDataTrialSettings
    """

    end_behavior: typing_extensions.Required[
        CheckoutSessionCreateBodySubscriptionDataTrialSettingsEndBehavior
    ]


class _SerializerCheckoutSessionCreateBodySubscriptionDataTrialSettings(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodySubscriptionDataTrialSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_behavior: _SerializerCheckoutSessionCreateBodySubscriptionDataTrialSettingsEndBehavior = pydantic.Field(
        alias="end_behavior",
    )
