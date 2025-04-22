import pydantic
import typing
import typing_extensions

from .payment_link_create_body_subscription_data_invoice_settings import (
    PaymentLinkCreateBodySubscriptionDataInvoiceSettings,
    _SerializerPaymentLinkCreateBodySubscriptionDataInvoiceSettings,
)
from .payment_link_create_body_subscription_data_metadata import (
    PaymentLinkCreateBodySubscriptionDataMetadata,
    _SerializerPaymentLinkCreateBodySubscriptionDataMetadata,
)
from .payment_link_create_body_subscription_data_trial_settings import (
    PaymentLinkCreateBodySubscriptionDataTrialSettings,
    _SerializerPaymentLinkCreateBodySubscriptionDataTrialSettings,
)


class PaymentLinkCreateBodySubscriptionData(typing_extensions.TypedDict):
    """
    When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
    """

    description: typing_extensions.NotRequired[str]

    invoice_settings: typing_extensions.NotRequired[
        PaymentLinkCreateBodySubscriptionDataInvoiceSettings
    ]

    metadata: typing_extensions.NotRequired[
        PaymentLinkCreateBodySubscriptionDataMetadata
    ]

    trial_period_days: typing_extensions.NotRequired[int]

    trial_settings: typing_extensions.NotRequired[
        PaymentLinkCreateBodySubscriptionDataTrialSettings
    ]


class _SerializerPaymentLinkCreateBodySubscriptionData(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodySubscriptionData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    invoice_settings: typing.Optional[
        _SerializerPaymentLinkCreateBodySubscriptionDataInvoiceSettings
    ] = pydantic.Field(alias="invoice_settings", default=None)
    metadata: typing.Optional[
        _SerializerPaymentLinkCreateBodySubscriptionDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    trial_period_days: typing.Optional[int] = pydantic.Field(
        alias="trial_period_days", default=None
    )
    trial_settings: typing.Optional[
        _SerializerPaymentLinkCreateBodySubscriptionDataTrialSettings
    ] = pydantic.Field(alias="trial_settings", default=None)
