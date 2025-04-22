import pydantic
import typing
import typing_extensions

from .payment_link_update_body_subscription_data_invoice_settings import (
    PaymentLinkUpdateBodySubscriptionDataInvoiceSettings,
    _SerializerPaymentLinkUpdateBodySubscriptionDataInvoiceSettings,
)
from .payment_link_update_body_subscription_data_metadata_obj0 import (
    PaymentLinkUpdateBodySubscriptionDataMetadataObj0,
    _SerializerPaymentLinkUpdateBodySubscriptionDataMetadataObj0,
)
from .payment_link_update_body_subscription_data_trial_settings_obj0 import (
    PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0,
    _SerializerPaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0,
)


class PaymentLinkUpdateBodySubscriptionData(typing_extensions.TypedDict):
    """
    When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
    """

    invoice_settings: typing_extensions.NotRequired[
        PaymentLinkUpdateBodySubscriptionDataInvoiceSettings
    ]

    metadata: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodySubscriptionDataMetadataObj0, str]
    ]

    trial_period_days: typing_extensions.NotRequired[typing.Union[int, str]]

    trial_settings: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0, str]
    ]


class _SerializerPaymentLinkUpdateBodySubscriptionData(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodySubscriptionData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    invoice_settings: typing.Optional[
        _SerializerPaymentLinkUpdateBodySubscriptionDataInvoiceSettings
    ] = pydantic.Field(alias="invoice_settings", default=None)
    metadata: typing.Optional[
        typing.Union[_SerializerPaymentLinkUpdateBodySubscriptionDataMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    trial_period_days: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="trial_period_days", default=None
    )
    trial_settings: typing.Optional[
        typing.Union[
            _SerializerPaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0, str
        ]
    ] = pydantic.Field(alias="trial_settings", default=None)
