import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_subscription_data_invoice_settings import (
    CheckoutSessionCreateBodySubscriptionDataInvoiceSettings,
    _SerializerCheckoutSessionCreateBodySubscriptionDataInvoiceSettings,
)
from .checkout_session_create_body_subscription_data_metadata import (
    CheckoutSessionCreateBodySubscriptionDataMetadata,
    _SerializerCheckoutSessionCreateBodySubscriptionDataMetadata,
)
from .checkout_session_create_body_subscription_data_transfer_data import (
    CheckoutSessionCreateBodySubscriptionDataTransferData,
    _SerializerCheckoutSessionCreateBodySubscriptionDataTransferData,
)
from .checkout_session_create_body_subscription_data_trial_settings import (
    CheckoutSessionCreateBodySubscriptionDataTrialSettings,
    _SerializerCheckoutSessionCreateBodySubscriptionDataTrialSettings,
)


class CheckoutSessionCreateBodySubscriptionData(typing_extensions.TypedDict):
    """
    A subset of parameters to be passed to subscription creation for Checkout Sessions in `subscription` mode.
    """

    application_fee_percent: typing_extensions.NotRequired[float]

    billing_cycle_anchor: typing_extensions.NotRequired[int]

    default_tax_rates: typing_extensions.NotRequired[typing.List[str]]

    description: typing_extensions.NotRequired[str]

    invoice_settings: typing_extensions.NotRequired[
        CheckoutSessionCreateBodySubscriptionDataInvoiceSettings
    ]

    metadata: typing_extensions.NotRequired[
        CheckoutSessionCreateBodySubscriptionDataMetadata
    ]

    on_behalf_of: typing_extensions.NotRequired[str]

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["create_prorations", "none"]
    ]

    transfer_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodySubscriptionDataTransferData
    ]

    trial_end: typing_extensions.NotRequired[int]

    trial_period_days: typing_extensions.NotRequired[int]

    trial_settings: typing_extensions.NotRequired[
        CheckoutSessionCreateBodySubscriptionDataTrialSettings
    ]


class _SerializerCheckoutSessionCreateBodySubscriptionData(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodySubscriptionData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    billing_cycle_anchor: typing.Optional[int] = pydantic.Field(
        alias="billing_cycle_anchor", default=None
    )
    default_tax_rates: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="default_tax_rates", default=None
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    invoice_settings: typing.Optional[
        _SerializerCheckoutSessionCreateBodySubscriptionDataInvoiceSettings
    ] = pydantic.Field(alias="invoice_settings", default=None)
    metadata: typing.Optional[
        _SerializerCheckoutSessionCreateBodySubscriptionDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    proration_behavior: typing.Optional[
        typing_extensions.Literal["create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    transfer_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodySubscriptionDataTransferData
    ] = pydantic.Field(alias="transfer_data", default=None)
    trial_end: typing.Optional[int] = pydantic.Field(alias="trial_end", default=None)
    trial_period_days: typing.Optional[int] = pydantic.Field(
        alias="trial_period_days", default=None
    )
    trial_settings: typing.Optional[
        _SerializerCheckoutSessionCreateBodySubscriptionDataTrialSettings
    ] = pydantic.Field(alias="trial_settings", default=None)
