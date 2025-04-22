import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_blik_display_preference import (
    PaymentMethodConfigurationUpdateBodyBlikDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyBlikDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyBlik(typing_extensions.TypedDict):
    """
    BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyBlikDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyBlik(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyBlik handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyBlikDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
