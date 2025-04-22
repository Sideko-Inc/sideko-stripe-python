import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_link_display_preference import (
    PaymentMethodConfigurationUpdateBodyLinkDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyLinkDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyLink(typing_extensions.TypedDict):
    """
    [Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyLinkDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyLink(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyLink handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyLinkDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
