import pydantic
import typing
import typing_extensions

from .subscription_schedule_update_body_default_settings_automatic_tax import (
    SubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTax,
    _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTax,
)
from .subscription_schedule_update_body_default_settings_invoice_settings import (
    SubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettings,
    _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettings,
)
from .subscription_schedule_update_body_default_settings_transfer_data_obj0 import (
    SubscriptionScheduleUpdateBodyDefaultSettingsTransferDataObj0,
    _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsTransferDataObj0,
)


class SubscriptionScheduleUpdateBodyDefaultSettings(typing_extensions.TypedDict):
    """
    Object representing the subscription schedule's default settings.
    """

    application_fee_percent: typing_extensions.NotRequired[float]

    automatic_tax: typing_extensions.NotRequired[
        SubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTax
    ]

    billing_cycle_anchor: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "phase_start"]
    ]

    collection_method: typing_extensions.NotRequired[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ]

    default_payment_method: typing_extensions.NotRequired[str]

    description: typing_extensions.NotRequired[typing.Union[str, str]]

    invoice_settings: typing_extensions.NotRequired[
        SubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettings
    ]

    on_behalf_of: typing_extensions.NotRequired[typing.Union[str, str]]

    transfer_data: typing_extensions.NotRequired[
        typing.Union[SubscriptionScheduleUpdateBodyDefaultSettingsTransferDataObj0, str]
    ]


class _SerializerSubscriptionScheduleUpdateBodyDefaultSettings(pydantic.BaseModel):
    """
    Serializer for SubscriptionScheduleUpdateBodyDefaultSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    automatic_tax: typing.Optional[
        _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsAutomaticTax
    ] = pydantic.Field(alias="automatic_tax", default=None)
    billing_cycle_anchor: typing.Optional[
        typing_extensions.Literal["automatic", "phase_start"]
    ] = pydantic.Field(alias="billing_cycle_anchor", default=None)
    collection_method: typing.Optional[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ] = pydantic.Field(alias="collection_method", default=None)
    default_payment_method: typing.Optional[str] = pydantic.Field(
        alias="default_payment_method", default=None
    )
    description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="description", default=None
    )
    invoice_settings: typing.Optional[
        _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettings
    ] = pydantic.Field(alias="invoice_settings", default=None)
    on_behalf_of: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    transfer_data: typing.Optional[
        typing.Union[
            _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsTransferDataObj0,
            str,
        ]
    ] = pydantic.Field(alias="transfer_data", default=None)
