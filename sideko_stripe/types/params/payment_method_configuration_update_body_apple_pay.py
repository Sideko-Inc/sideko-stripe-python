import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_apple_pay_display_preference import (
    PaymentMethodConfigurationUpdateBodyApplePayDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyApplePayDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyApplePay(typing_extensions.TypedDict):
    """
    Stripe users can accept [Apple Pay](/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyApplePayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyApplePay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyApplePay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyApplePayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
