import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_billie_display_preference import (
    PaymentMethodConfigurationUpdateBodyBillieDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyBillieDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyBillie(typing_extensions.TypedDict):
    """
    Billie is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method that offers businesses Pay by Invoice where they offer payment terms ranging from 7-120 days. Customers are redirected from your website or app, authorize the payment with Billie, then return to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyBillieDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyBillie(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyBillie handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyBillieDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
