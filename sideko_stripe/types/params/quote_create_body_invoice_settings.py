import pydantic
import typing
import typing_extensions

from .quote_create_body_invoice_settings_issuer import (
    QuoteCreateBodyInvoiceSettingsIssuer,
    _SerializerQuoteCreateBodyInvoiceSettingsIssuer,
)


class QuoteCreateBodyInvoiceSettings(typing_extensions.TypedDict):
    """
    All invoices will be billed using the specified settings.
    """

    days_until_due: typing_extensions.NotRequired[int]

    issuer: typing_extensions.NotRequired[QuoteCreateBodyInvoiceSettingsIssuer]


class _SerializerQuoteCreateBodyInvoiceSettings(pydantic.BaseModel):
    """
    Serializer for QuoteCreateBodyInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    days_until_due: typing.Optional[int] = pydantic.Field(
        alias="days_until_due", default=None
    )
    issuer: typing.Optional[_SerializerQuoteCreateBodyInvoiceSettingsIssuer] = (
        pydantic.Field(alias="issuer", default=None)
    )
