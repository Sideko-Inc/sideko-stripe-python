import pydantic
import typing
import typing_extensions

from .customer_subscription_modify_body_invoice_settings_issuer import (
    CustomerSubscriptionModifyBodyInvoiceSettingsIssuer,
    _SerializerCustomerSubscriptionModifyBodyInvoiceSettingsIssuer,
)


class CustomerSubscriptionModifyBodyInvoiceSettings(typing_extensions.TypedDict):
    """
    All invoices will be billed using the specified settings.
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    issuer: typing_extensions.NotRequired[
        CustomerSubscriptionModifyBodyInvoiceSettingsIssuer
    ]


class _SerializerCustomerSubscriptionModifyBodyInvoiceSettings(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionModifyBodyInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_tax_ids: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="account_tax_ids", default=None)
    )
    issuer: typing.Optional[
        _SerializerCustomerSubscriptionModifyBodyInvoiceSettingsIssuer
    ] = pydantic.Field(alias="issuer", default=None)
