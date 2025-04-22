import pydantic
import typing
import typing_extensions

from .billing_portal_configuration_update_body_features_subscription_cancel_cancellation_reason import (
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancelCancellationReason,
    _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancelCancellationReason,
)


class BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancel(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancel
    """

    cancellation_reason: typing_extensions.NotRequired[
        BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancelCancellationReason
    ]

    enabled: typing_extensions.NotRequired[bool]

    mode: typing_extensions.NotRequired[
        typing_extensions.Literal["at_period_end", "immediately"]
    ]

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]


class _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancel(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancel handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cancellation_reason: typing.Optional[
        _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancelCancellationReason
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    mode: typing.Optional[typing_extensions.Literal["at_period_end", "immediately"]] = (
        pydantic.Field(alias="mode", default=None)
    )
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
