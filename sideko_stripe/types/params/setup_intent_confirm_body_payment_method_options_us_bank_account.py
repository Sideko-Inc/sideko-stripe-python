import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_options_us_bank_account_financial_connections import (
    SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnections,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnections,
)
from .setup_intent_confirm_body_payment_method_options_us_bank_account_mandate_options import (
    SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountMandateOptions,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountMandateOptions,
)
from .setup_intent_confirm_body_payment_method_options_us_bank_account_networks import (
    SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountNetworks,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountNetworks,
)


class SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccount(
    typing_extensions.TypedDict
):
    """
    SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccount
    """

    financial_connections: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    ]

    mandate_options: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountMandateOptions
    ]

    networks: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountNetworks
    ]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccount(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    financial_connections: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    ] = pydantic.Field(alias="financial_connections", default=None)
    mandate_options: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    networks: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountNetworks
    ] = pydantic.Field(alias="networks", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
