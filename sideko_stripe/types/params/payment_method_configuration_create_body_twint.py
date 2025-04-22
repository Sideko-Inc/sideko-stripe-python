import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_twint_display_preference import (
    PaymentMethodConfigurationCreateBodyTwintDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyTwintDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyTwint(typing_extensions.TypedDict):
    """
    Twint is a payment method popular in Switzerland. It allows customers to pay using their mobile phone. Check this [page](https://docs.stripe.com/payments/twint) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyTwintDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyTwint(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyTwint handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyTwintDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
