import pydantic
import typing
import typing_extensions

from .billing_portal_configuration_update_body_features_customer_update import (
    BillingPortalConfigurationUpdateBodyFeaturesCustomerUpdate,
    _SerializerBillingPortalConfigurationUpdateBodyFeaturesCustomerUpdate,
)
from .billing_portal_configuration_update_body_features_invoice_history import (
    BillingPortalConfigurationUpdateBodyFeaturesInvoiceHistory,
    _SerializerBillingPortalConfigurationUpdateBodyFeaturesInvoiceHistory,
)
from .billing_portal_configuration_update_body_features_payment_method_update import (
    BillingPortalConfigurationUpdateBodyFeaturesPaymentMethodUpdate,
    _SerializerBillingPortalConfigurationUpdateBodyFeaturesPaymentMethodUpdate,
)
from .billing_portal_configuration_update_body_features_subscription_cancel import (
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancel,
    _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancel,
)
from .billing_portal_configuration_update_body_features_subscription_update import (
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdate,
    _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdate,
)


class BillingPortalConfigurationUpdateBodyFeatures(typing_extensions.TypedDict):
    """
    Information about the features available in the portal.
    """

    customer_update: typing_extensions.NotRequired[
        BillingPortalConfigurationUpdateBodyFeaturesCustomerUpdate
    ]

    invoice_history: typing_extensions.NotRequired[
        BillingPortalConfigurationUpdateBodyFeaturesInvoiceHistory
    ]

    payment_method_update: typing_extensions.NotRequired[
        BillingPortalConfigurationUpdateBodyFeaturesPaymentMethodUpdate
    ]

    subscription_cancel: typing_extensions.NotRequired[
        BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancel
    ]

    subscription_update: typing_extensions.NotRequired[
        BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdate
    ]


class _SerializerBillingPortalConfigurationUpdateBodyFeatures(pydantic.BaseModel):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_update: typing.Optional[
        _SerializerBillingPortalConfigurationUpdateBodyFeaturesCustomerUpdate
    ] = pydantic.Field(alias="customer_update", default=None)
    invoice_history: typing.Optional[
        _SerializerBillingPortalConfigurationUpdateBodyFeaturesInvoiceHistory
    ] = pydantic.Field(alias="invoice_history", default=None)
    payment_method_update: typing.Optional[
        _SerializerBillingPortalConfigurationUpdateBodyFeaturesPaymentMethodUpdate
    ] = pydantic.Field(alias="payment_method_update", default=None)
    subscription_cancel: typing.Optional[
        _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancel
    ] = pydantic.Field(alias="subscription_cancel", default=None)
    subscription_update: typing.Optional[
        _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdate
    ] = pydantic.Field(alias="subscription_update", default=None)
