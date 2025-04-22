import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_swish_display_preference import (
    PaymentMethodConfigurationUpdateBodySwishDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodySwishDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodySwish(typing_extensions.TypedDict):
    """
    Swish is a [real-time](https://stripe.com/docs/payments/real-time) payment method popular in Sweden. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the Swish mobile app and the Swedish BankID mobile app. Check this [page](https://stripe.com/docs/payments/swish) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodySwishDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodySwish(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodySwish handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodySwishDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
