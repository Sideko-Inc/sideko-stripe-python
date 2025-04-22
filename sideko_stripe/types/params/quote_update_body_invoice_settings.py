import pydantic
import typing
import typing_extensions

from .quote_update_body_invoice_settings_issuer import (
    QuoteUpdateBodyInvoiceSettingsIssuer,
    _SerializerQuoteUpdateBodyInvoiceSettingsIssuer,
)


class QuoteUpdateBodyInvoiceSettings(typing_extensions.TypedDict):
    """
    All invoices will be billed using the specified settings.
    """

    days_until_due: typing_extensions.NotRequired[int]

    issuer: typing_extensions.NotRequired[QuoteUpdateBodyInvoiceSettingsIssuer]


class _SerializerQuoteUpdateBodyInvoiceSettings(pydantic.BaseModel):
    """
    Serializer for QuoteUpdateBodyInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    days_until_due: typing.Optional[int] = pydantic.Field(
        alias="days_until_due", default=None
    )
    issuer: typing.Optional[_SerializerQuoteUpdateBodyInvoiceSettingsIssuer] = (
        pydantic.Field(alias="issuer", default=None)
    )
