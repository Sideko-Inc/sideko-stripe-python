import pydantic
import typing
import typing_extensions

from .payment_link_update_body_subscription_data_invoice_settings_issuer import (
    PaymentLinkUpdateBodySubscriptionDataInvoiceSettingsIssuer,
    _SerializerPaymentLinkUpdateBodySubscriptionDataInvoiceSettingsIssuer,
)


class PaymentLinkUpdateBodySubscriptionDataInvoiceSettings(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodySubscriptionDataInvoiceSettings
    """

    issuer: typing_extensions.NotRequired[
        PaymentLinkUpdateBodySubscriptionDataInvoiceSettingsIssuer
    ]


class _SerializerPaymentLinkUpdateBodySubscriptionDataInvoiceSettings(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkUpdateBodySubscriptionDataInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    issuer: typing.Optional[
        _SerializerPaymentLinkUpdateBodySubscriptionDataInvoiceSettingsIssuer
    ] = pydantic.Field(alias="issuer", default=None)
