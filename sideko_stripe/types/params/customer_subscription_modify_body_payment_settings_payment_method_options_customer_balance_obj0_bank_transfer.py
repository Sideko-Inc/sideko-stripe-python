import pydantic
import typing
import typing_extensions

from .customer_subscription_modify_body_payment_settings_payment_method_options_customer_balance_obj0_bank_transfer_eu_bank_transfer import (
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
    _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
)


class CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    """

    eu_bank_transfer: typing_extensions.NotRequired[
        CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ]

    type_: typing_extensions.NotRequired[str]


class _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ] = pydantic.Field(alias="eu_bank_transfer", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
