import pydantic
import typing
import typing_extensions

from .payment_method_configuration_create_body_us_bank_account_display_preference import (
    PaymentMethodConfigurationCreateBodyUsBankAccountDisplayPreference,
    _SerializerPaymentMethodConfigurationCreateBodyUsBankAccountDisplayPreference,
)


class PaymentMethodConfigurationCreateBodyUsBankAccount(typing_extensions.TypedDict):
    """
    Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-direct-debit) for more details.
    """

    display_preference: typing_extensions.NotRequired[
        PaymentMethodConfigurationCreateBodyUsBankAccountDisplayPreference
    ]


class _SerializerPaymentMethodConfigurationCreateBodyUsBankAccount(pydantic.BaseModel):
    """
    Serializer for PaymentMethodConfigurationCreateBodyUsBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    display_preference: typing.Optional[
        _SerializerPaymentMethodConfigurationCreateBodyUsBankAccountDisplayPreference
    ] = pydantic.Field(alias="display_preference", default=None)
