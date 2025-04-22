import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_blik_display_preference import (
    PaymentMethodConfigurationCreateBodyBlikDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyBlikDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyBlik(typing_extensions.TypedDict):
    """
    BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyBlikDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyBlik(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyBlik handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyBlikDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
