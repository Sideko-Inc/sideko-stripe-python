import pydantic
import typing
import typing_extensions

from .customer_subscription_modify_body_payment_settings_payment_method_options_customer_balance_obj0_bank_transfer import (
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
    _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
)


class CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0
    """

    bank_transfer: typing_extensions.NotRequired[
        CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ]

    funding_type: typing_extensions.NotRequired[str]


class _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_transfer: typing.Optional[
        _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ] = pydantic.Field(alias="bank_transfer", default=None)
    funding_type: typing.Optional[str] = pydantic.Field(
        alias="funding_type", default=None
    )
