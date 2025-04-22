import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_sofort_display_preference import (
    PaymentMethodConfigurationCreateBodySofortDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodySofortDisplayPreference,
)


class PaymentMethodConfigurationCreateBodySofort(typing_extensions.TypedDict):
    """
    Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodySofortDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodySofort(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodySofort handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodySofortDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
