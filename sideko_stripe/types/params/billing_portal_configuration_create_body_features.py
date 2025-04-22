import pydantic
import typing
import typing_extensions

from .billing_portal_configuration_create_body_features_customer_update import (
    BillingPortalConfigurationCreateBodyFeaturesCustomerUpdate,
    _SerializerBillingPortalConfigurationCreateBodyFeaturesCustomerUpdate,
)
from .billing_portal_configuration_create_body_features_invoice_history import (
    BillingPortalConfigurationCreateBodyFeaturesInvoiceHistory,
    _SerializerBillingPortalConfigurationCreateBodyFeaturesInvoiceHistory,
)
from .billing_portal_configuration_create_body_features_payment_method_update import (
    BillingPortalConfigurationCreateBodyFeaturesPaymentMethodUpdate,
    _SerializerBillingPortalConfigurationCreateBodyFeaturesPaymentMethodUpdate,
)
from .billing_portal_configuration_create_body_features_subscription_cancel import (
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancel,
    _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionCancel,
)
from .billing_portal_configuration_create_body_features_subscription_update import (
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdate,
    _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdate,
)


class BillingPortalConfigurationCreateBodyFeatures(typing_extensions.TypedDict):
    """
    Information about the features available in the portal.
    """

    customer_update: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyFeaturesCustomerUpdate
    ]

    invoice_history: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyFeaturesInvoiceHistory
    ]

    payment_method_update: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyFeaturesPaymentMethodUpdate
    ]

    subscription_cancel: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancel
    ]

    subscription_update: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdate
    ]


class _SerializerBillingPortalConfigurationCreateBodyFeatures(pydantic.BaseModel):
    """
    Serializer for BillingPortalConfigurationCreateBodyFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_update: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyFeaturesCustomerUpdate
    ] = pydantic.Field(alias="customer_update", default=None)
    invoice_history: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyFeaturesInvoiceHistory
    ] = pydantic.Field(alias="invoice_history", default=None)
    payment_method_update: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyFeaturesPaymentMethodUpdate
    ] = pydantic.Field(alias="payment_method_update", default=None)
    subscription_cancel: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionCancel
    ] = pydantic.Field(alias="subscription_cancel", default=None)
    subscription_update: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdate
    ] = pydantic.Field(alias="subscription_update", default=None)
