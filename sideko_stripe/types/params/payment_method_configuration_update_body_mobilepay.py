import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_mobilepay_display_preference import (
    PaymentMethodConfigurationUpdateBodyMobilepayDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyMobilepayDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyMobilepay(typing_extensions.TypedDict):
    """
    MobilePay is a [single-use](https://stripe.com/docs/payments/payment-methods#usage) card wallet payment method used in Denmark and Finland. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the MobilePay app. Check this [page](https://stripe.com/docs/payments/mobilepay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyMobilepayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyMobilepay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyMobilepay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyMobilepayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
