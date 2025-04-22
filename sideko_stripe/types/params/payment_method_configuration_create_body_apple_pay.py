import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_apple_pay_display_preference import (
    PaymentMethodConfigurationCreateBodyApplePayDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyApplePayDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyApplePay(typing_extensions.TypedDict):
    """
    Stripe users can accept [Apple Pay](/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyApplePayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyApplePay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyApplePay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyApplePayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
