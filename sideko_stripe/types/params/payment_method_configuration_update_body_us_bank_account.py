import pydantic
import typing
import typing_extensions

from .payment_method_configuration_update_body_us_bank_account_display_preference import (
    PaymentMethodConfigurationUpdateBodyUsBankAccountDisplayPreference,
    _SerializerPaymentMethodConfigurationUpdateBodyUsBankAccountDisplayPreference,
)


class PaymentMethodConfigurationUpdateBodyUsBankAccount(typing_extensions.TypedDict):
    """
    Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-direct-debit) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationUpdateBodyUsBankAccountDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationUpdateBodyUsBankAccount(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationUpdateBodyUsBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationUpdateBodyUsBankAccountDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
