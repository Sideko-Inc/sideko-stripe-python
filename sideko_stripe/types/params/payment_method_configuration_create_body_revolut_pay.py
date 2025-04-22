import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_revolut_pay_display_preference import (
    PaymentMethodConfigurationCreateBodyRevolutPayDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyRevolutPayDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyRevolutPay(typing_extensions.TypedDict):
    """
    Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyRevolutPayDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyRevolutPay(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyRevolutPay handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyRevolutPayDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
