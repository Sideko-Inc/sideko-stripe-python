import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_options_us_bank_account_financial_connections_filters import (
    SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
)


class SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnections(
    typing_extensions.TypedDict
):
    """
    SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    """

    filters: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters
    ]

    permissions: typing_extensions.NotRequired[
        typing.List[
            typing_extensions.Literal[
                "balances", "ownership", "payment_method", "transactions"
            ]
        ]
    ]

    prefetch: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["balances", "ownership", "transactions"]]
    ]

    return_url: typing_extensions.NotRequired[str]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnections(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnections handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    filters: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters
    ] = pydantic.Field(alias="filters", default=None)
    permissions: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "balances", "ownership", "payment_method", "transactions"
            ]
        ]
    ] = pydantic.Field(alias="permissions", default=None)
    prefetch: typing.Optional[
        typing.List[typing_extensions.Literal["balances", "ownership", "transactions"]]
    ] = pydantic.Field(alias="prefetch", default=None)
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
