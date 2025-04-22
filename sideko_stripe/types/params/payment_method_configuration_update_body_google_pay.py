import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_google_pay_display_preference import (
    PaymentMethodConfigurationUpdateBodyGooglePayDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyGooglePayDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyGooglePay(typing_extensions.TypedDict):
    """
    Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyGooglePayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyGooglePay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyGooglePay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyGooglePayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
