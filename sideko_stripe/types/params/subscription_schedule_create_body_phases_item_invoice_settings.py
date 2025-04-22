import pydantic
import typing
import typing_extensions

from .subscription_schedule_create_body_phases_item_invoice_settings_issuer import (
    SubscriptionScheduleCreateBodyPhasesItemInvoiceSettingsIssuer,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemInvoiceSettingsIssuer,
)


class SubscriptionScheduleCreateBodyPhasesItemInvoiceSettings(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleCreateBodyPhasesItemInvoiceSettings
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    days_until_due: typing_extensions.NotRequired[int]

    issuer: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyPhasesItemInvoiceSettingsIssuer
    ]


class _SerializerSubscriptionScheduleCreateBodyPhasesItemInvoiceSettings(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItemInvoiceSettings handling case conversions
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
        _SerializerSubscriptionScheduleCreateBodyPhasesItemInvoiceSettingsIssuer
    ] = pydantic.Field(alias="issuer", default=None)
