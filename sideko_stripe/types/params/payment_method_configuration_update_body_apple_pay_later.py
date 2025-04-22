import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_apple_pay_later_display_preference import (
    PaymentMethodConfigurationUpdateBodyApplePayLaterDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyApplePayLaterDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyApplePayLater(typing_extensions.TypedDict):
    """
    Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyApplePayLaterDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyApplePayLater(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyApplePayLater handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyApplePayLaterDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
