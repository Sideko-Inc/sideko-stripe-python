import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_satispay_display_preference import (
    PaymentMethodConfigurationCreateBodySatispayDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodySatispayDisplayPreference,
)


class PaymentMethodConfigurationCreateBodySatispay(typing_extensions.TypedDict):
    """
    Satispay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method where customers are required to [authenticate](/payments/payment-methods#customer-actions) their payment. Customers pay by being redirected from your website or app, authorizing the payment with Satispay, then returning to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodySatispayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodySatispay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodySatispay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodySatispayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
