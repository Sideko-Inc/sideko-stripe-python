import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_p24_display_preference import (
    PaymentMethodConfigurationCreateBodyP24DisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyP24DisplayPreference,
)


class PaymentMethodConfigurationCreateBodyP24(typing_extensions.TypedDict):
    """
    Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyP24DisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyP24(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyP24 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyP24DisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
