import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_options_us_bank_account_financial_connections_filters import (
    SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters,
)


class SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnections(
    typing_extensions.TypedDict
):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    """

    filters: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters
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


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnections(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnections handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    filters: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters
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
