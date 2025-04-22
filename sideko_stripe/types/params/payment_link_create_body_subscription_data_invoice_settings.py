import pydantic
import typing
import typing_extensions

from .payment_link_create_body_subscription_data_invoice_settings_issuer import (
    PaymentLinkCreateBodySubscriptionDataInvoiceSettingsIssuer,
    _SerializerPaymentLinkCreateBodySubscriptionDataInvoiceSettingsIssuer,
)


class PaymentLinkCreateBodySubscriptionDataInvoiceSettings(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodySubscriptionDataInvoiceSettings
    """

    issuer: typing_extensions.NotRequired[
        PaymentLinkCreateBodySubscriptionDataInvoiceSettingsIssuer
    ]


class _SerializerPaymentLinkCreateBodySubscriptionDataInvoiceSettings(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkCreateBodySubscriptionDataInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    issuer: typing.Optional[
        _SerializerPaymentLinkCreateBodySubscriptionDataInvoiceSettingsIssuer
    ] = pydantic.Field(alias="issuer", default=None)
