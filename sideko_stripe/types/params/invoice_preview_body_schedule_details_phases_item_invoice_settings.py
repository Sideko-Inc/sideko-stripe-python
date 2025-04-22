import pydantic
import typing
import typing_extensions

from .invoice_preview_body_schedule_details_phases_item_invoice_settings_issuer import (
    InvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettingsIssuer,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettingsIssuer,
)


class InvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettings(
    typing_extensions.TypedDict
):
    """
    InvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettings
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    days_until_due: typing_extensions.NotRequired[int]

    issuer: typing_extensions.NotRequired[
        InvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettingsIssuer
    ]


class _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettings(
    pydantic.BaseModel
):
    """
    Serializer for InvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettings handling case conversions
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
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettingsIssuer
    ] = pydantic.Field(alias="issuer", default=None)
