import pydantic
import typing
import typing_extensions

from .customer_subscription_create_body_invoice_settings_issuer import (
    CustomerSubscriptionCreateBodyInvoiceSettingsIssuer,
    _SerializerCustomerSubscriptionCreateBodyInvoiceSettingsIssuer,
)


class CustomerSubscriptionCreateBodyInvoiceSettings(typing_extensions.TypedDict):
    """
    All invoices will be billed using the specified settings.
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    issuer: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyInvoiceSettingsIssuer
    ]


class _SerializerCustomerSubscriptionCreateBodyInvoiceSettings(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionCreateBodyInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_tax_ids: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="account_tax_ids", default=None)
    )
    issuer: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyInvoiceSettingsIssuer
    ] = pydantic.Field(alias="issuer", default=None)
