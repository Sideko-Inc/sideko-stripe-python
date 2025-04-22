import pydantic
import typing
import typing_extensions

from .billing_portal_configuration_create_body_features_subscription_cancel_cancellation_reason import (
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancelCancellationReason,
    _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionCancelCancellationReason,
)


class BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancel(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancel
    """

    cancellation_reason: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancelCancellationReason
    ]

    enabled: typing_extensions.Required[bool]

    mode: typing_extensions.NotRequired[
        typing_extensions.Literal["at_period_end", "immediately"]
    ]

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]


class _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionCancel(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancel handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cancellation_reason: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionCancelCancellationReason
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    mode: typing.Optional[typing_extensions.Literal["at_period_end", "immediately"]] = (
        pydantic.Field(alias="mode", default=None)
    )
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
