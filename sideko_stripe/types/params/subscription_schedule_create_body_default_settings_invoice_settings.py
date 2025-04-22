import pydantic
import typing
import typing_extensions

from .subscription_schedule_create_body_default_settings_invoice_settings_issuer import (
    SubscriptionScheduleCreateBodyDefaultSettingsInvoiceSettingsIssuer,
    _SerializerSubscriptionScheduleCreateBodyDefaultSettingsInvoiceSettingsIssuer,
)


class SubscriptionScheduleCreateBodyDefaultSettingsInvoiceSettings(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleCreateBodyDefaultSettingsInvoiceSettings
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    days_until_due: typing_extensions.NotRequired[int]

    issuer: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyDefaultSettingsInvoiceSettingsIssuer
    ]


class _SerializerSubscriptionScheduleCreateBodyDefaultSettingsInvoiceSettings(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleCreateBodyDefaultSettingsInvoiceSettings handling case conversions
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
        _SerializerSubscriptionScheduleCreateBodyDefaultSettingsInvoiceSettingsIssuer
    ] = pydantic.Field(alias="issuer", default=None)
