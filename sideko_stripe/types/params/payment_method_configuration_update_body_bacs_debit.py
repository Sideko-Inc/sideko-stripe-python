import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_bacs_debit_display_preference import (
    PaymentMethodConfigurationUpdateBodyBacsDebitDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyBacsDebitDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyBacsDebit(typing_extensions.TypedDict):
    """
    Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyBacsDebitDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyBacsDebit(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyBacsDebitDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
