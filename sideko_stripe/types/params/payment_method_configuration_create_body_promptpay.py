import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_promptpay_display_preference import (
    PaymentMethodConfigurationCreateBodyPromptpayDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyPromptpayDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyPromptpay(typing_extensions.TypedDict):
    """
    PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyPromptpayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyPromptpay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyPromptpay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyPromptpayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
