import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_eps_display_preference import (
    PaymentMethodConfigurationCreateBodyEpsDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyEpsDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyEps(typing_extensions.TypedDict):
    """
    EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyEpsDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyEps(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyEps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyEpsDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
