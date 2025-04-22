import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_paypal_display_preference import (
    PaymentMethodConfigurationUpdateBodyPaypalDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyPaypalDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyPaypal(typing_extensions.TypedDict):
    """
    PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyPaypalDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyPaypal(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyPaypal handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyPaypalDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
