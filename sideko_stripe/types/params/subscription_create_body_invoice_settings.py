import pydantic
import typing
import typing_extensions

from .subscription_create_body_invoice_settings_issuer import (
    SubscriptionCreateBodyInvoiceSettingsIssuer,
    _SerializerSubscriptionCreateBodyInvoiceSettingsIssuer,
)


class SubscriptionCreateBodyInvoiceSettings(typing_extensions.TypedDict):
    """
    All invoices will be billed using the specified settings.
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    issuer: typing_extensions.NotRequired[SubscriptionCreateBodyInvoiceSettingsIssuer]


class _SerializerSubscriptionCreateBodyInvoiceSettings(pydantic.BaseModel):
    """
    Serializer for SubscriptionCreateBodyInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_tax_ids: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="account_tax_ids", default=None)
    )
    issuer: typing.Optional[_SerializerSubscriptionCreateBodyInvoiceSettingsIssuer] = (
        pydantic.Field(alias="issuer", default=None)
    )
