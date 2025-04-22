import pydantic
import typing
import typing_extensions

from .customer_subscription_create_body_payment_settings_payment_method_options_customer_balance_obj0_bank_transfer import (
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
    _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
)


class CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0
    """

    bank_transfer: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ]

    funding_type: typing_extensions.NotRequired[str]


class _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_transfer: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ] = pydantic.Field(alias="bank_transfer", default=None)
    funding_type: typing.Optional[str] = pydantic.Field(
        alias="funding_type", default=None
    )
