import pydantic
import typing_extensions

from .payment_link_create_body_subscription_data_trial_settings_end_behavior import (
    PaymentLinkCreateBodySubscriptionDataTrialSettingsEndBehavior,
    _SerializerPaymentLinkCreateBodySubscriptionDataTrialSettingsEndBehavior,
)


class PaymentLinkCreateBodySubscriptionDataTrialSettings(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodySubscriptionDataTrialSettings
    """

    end_behavior: typing_extensions.Required[
        PaymentLinkCreateBodySubscriptionDataTrialSettingsEndBehavior
    ]


class _SerializerPaymentLinkCreateBodySubscriptionDataTrialSettings(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodySubscriptionDataTrialSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_behavior: _SerializerPaymentLinkCreateBodySubscriptionDataTrialSettingsEndBehavior = pydantic.Field(
        alias="end_behavior",
    )
