import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_payment_method_options_us_bank_account_financial_connections import (
    SetupIntentCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections,
)
from .setup_intent_create_body_payment_method_options_us_bank_account_mandate_options import (
    SetupIntentCreateBodyPaymentMethodOptionsUsBankAccountMandateOptions,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsUsBankAccountMandateOptions,
)
from .setup_intent_create_body_payment_method_options_us_bank_account_networks import (
    SetupIntentCreateBodyPaymentMethodOptionsUsBankAccountNetworks,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsUsBankAccountNetworks,
)


class SetupIntentCreateBodyPaymentMethodOptionsUsBankAccount(
    typing_extensions.TypedDict
):
    """
    SetupIntentCreateBodyPaymentMethodOptionsUsBankAccount
    """

    financial_connections: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    ]

    mandate_options: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsUsBankAccountMandateOptions
    ]

    networks: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsUsBankAccountNetworks
    ]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerSetupIntentCreateBodyPaymentMethodOptionsUsBankAccount(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodOptionsUsBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    financial_connections: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    ] = pydantic.Field(alias="financial_connections", default=None)
    mandate_options: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsUsBankAccountMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    networks: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsUsBankAccountNetworks
    ] = pydantic.Field(alias="networks", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
