import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_sofort_display_preference import (
    PaymentMethodConfigurationUpdateBodySofortDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodySofortDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodySofort(typing_extensions.TypedDict):
    """
    Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodySofortDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodySofort(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodySofort handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodySofortDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
