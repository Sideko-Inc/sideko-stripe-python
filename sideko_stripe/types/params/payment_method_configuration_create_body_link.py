import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_link_display_preference import (
    PaymentMethodConfigurationCreateBodyLinkDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyLinkDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyLink(typing_extensions.TypedDict):
    """
    [Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyLinkDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyLink(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyLink handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyLinkDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
