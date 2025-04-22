import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_card_display_preference import (
    PaymentMethodConfigurationCreateBodyCardDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyCardDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyCard(typing_extensions.TypedDict):
    """
    Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyCardDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyCard(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyCard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyCardDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
