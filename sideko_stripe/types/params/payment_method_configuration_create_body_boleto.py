import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_boleto_display_preference import (
    PaymentMethodConfigurationCreateBodyBoletoDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyBoletoDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyBoleto(typing_extensions.TypedDict):
    """
    Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyBoletoDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyBoleto(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyBoletoDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
