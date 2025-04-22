import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_bacs_debit_display_preference import (
    PaymentMethodConfigurationCreateBodyBacsDebitDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyBacsDebitDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyBacsDebit(typing_extensions.TypedDict):
    """
    Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyBacsDebitDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyBacsDebit(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyBacsDebitDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
