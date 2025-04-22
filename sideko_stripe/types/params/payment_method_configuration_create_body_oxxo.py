import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_oxxo_display_preference import (
    PaymentMethodConfigurationCreateBodyOxxoDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyOxxoDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyOxxo(typing_extensions.TypedDict):
    """
    OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyOxxoDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyOxxo(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyOxxo handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyOxxoDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
