import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_options_us_bank_account_financial_connections import (
    SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnections,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnections,
)
from .setup_intent_update_body_payment_method_options_us_bank_account_mandate_options import (
    SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountMandateOptions,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountMandateOptions,
)
from .setup_intent_update_body_payment_method_options_us_bank_account_networks import (
    SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountNetworks,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountNetworks,
)


class SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccount(
    typing_extensions.TypedDict
):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccount
    """

    financial_connections: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    ]

    mandate_options: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountMandateOptions
    ]

    networks: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountNetworks
    ]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccount(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    financial_connections: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    ] = pydantic.Field(alias="financial_connections", default=None)
    mandate_options: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    networks: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountNetworks
    ] = pydantic.Field(alias="networks", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
