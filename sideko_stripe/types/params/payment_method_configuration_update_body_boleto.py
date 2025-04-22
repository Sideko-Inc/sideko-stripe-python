import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_boleto_display_preference import (
    PaymentMethodConfigurationUpdateBodyBoletoDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyBoletoDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyBoleto(typing_extensions.TypedDict):
    """
    Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyBoletoDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyBoleto(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyBoleto handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyBoletoDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
