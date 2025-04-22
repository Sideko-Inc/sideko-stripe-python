import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_twint_display_preference import (
    PaymentMethodConfigurationUpdateBodyTwintDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyTwintDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyTwint(typing_extensions.TypedDict):
    """
    Twint is a payment method popular in Switzerland. It allows customers to pay using their mobile phone. Check this [page](https://docs.stripe.com/payments/twint) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyTwintDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyTwint(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyTwint handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyTwintDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
