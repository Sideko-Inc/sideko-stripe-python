import pydantic
import typing_extensions

from .payment_link_update_body_subscription_data_trial_settings_obj0_end_behavior import (
    PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0EndBehavior,
    _SerializerPaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0EndBehavior,
)


class PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0(
    typing_extensions.TypedDict
):
    """
    PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0
    """

    end_behavior: typing_extensions.Required[
        PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0EndBehavior
    ]


class _SerializerPaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_behavior: _SerializerPaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0EndBehavior = pydantic.Field(
        alias="end_behavior",
    )
