import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_subscription_data_invoice_settings_issuer import (
    CheckoutSessionCreateBodySubscriptionDataInvoiceSettingsIssuer,
    _SerializerCheckoutSessionCreateBodySubscriptionDataInvoiceSettingsIssuer,
)


class CheckoutSessionCreateBodySubscriptionDataInvoiceSettings(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodySubscriptionDataInvoiceSettings
    """

    issuer: typing_extensions.NotRequired[
        CheckoutSessionCreateBodySubscriptionDataInvoiceSettingsIssuer
    ]


class _SerializerCheckoutSessionCreateBodySubscriptionDataInvoiceSettings(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodySubscriptionDataInvoiceSettings handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    issuer: typing.Optional[
        _SerializerCheckoutSessionCreateBodySubscriptionDataInvoiceSettingsIssuer
    ] = pydantic.Field(alias="issuer", default=None)
