import pydantic
import typing
import typing_extensions

from .subscription_schedule_update_body_default_settings_invoice_settings_issuer import (
    SubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettingsIssuer,
    _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettingsIssuer,
)


class SubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettings(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettings
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    days_until_due: typing_extensions.NotRequired[int]

    issuer: typing_extensions.NotRequired[
        SubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettingsIssuer
    ]


class _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettings(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_tax_ids: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="account_tax_ids", default=None)
    )
    days_until_due: typing.Optional[int] = pydantic.Field(
        alias="days_until_due", default=None
    )
    issuer: typing.Optional[
        _SerializerSubscriptionScheduleUpdateBodyDefaultSettingsInvoiceSettingsIssuer
    ] = pydantic.Field(alias="issuer", default=None)
