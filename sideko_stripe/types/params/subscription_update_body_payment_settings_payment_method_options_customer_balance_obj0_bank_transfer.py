import pydantic
import typing
import typing_extensions

from .subscription_update_body_payment_settings_payment_method_options_customer_balance_obj0_bank_transfer_eu_bank_transfer import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer,
)


class SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    typing_extensions.TypedDict
):
    """
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    """

    eu_bank_transfer: typing_extensions.NotRequired[
        SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ]

    type_: typing_extensions.NotRequired[str]


class _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransfer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    eu_bank_transfer: typing.Optional[
        _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsCustomerBalanceObj0BankTransferEuBankTransfer
    ] = pydantic.Field(alias="eu_bank_transfer", default=None)
    type_: typing.Optional[str] = pydantic.Field(alias="type", default=None)
