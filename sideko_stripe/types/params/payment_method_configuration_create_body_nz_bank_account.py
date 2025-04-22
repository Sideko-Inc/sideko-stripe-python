import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_nz_bank_account_display_preference import (
    PaymentMethodConfigurationCreateBodyNzBankAccountDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyNzBankAccountDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyNzBankAccount(typing_extensions.TypedDict):
    """
    Stripe users in New Zealand can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with a New Zeland bank account. Check this [page](https://stripe.com/docs/payments/nz-bank-account) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyNzBankAccountDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyNzBankAccount(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyNzBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyNzBankAccountDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
