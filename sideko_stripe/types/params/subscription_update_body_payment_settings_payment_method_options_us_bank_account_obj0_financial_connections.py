import pydantic
import typing
import typing_extensions

from .subscription_update_body_payment_settings_payment_method_options_us_bank_account_obj0_financial_connections_filters import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters,
)


class SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections(
    typing_extensions.TypedDict
):
    """
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections
    """

    filters: typing_extensions.NotRequired[
        SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters
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


class _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    filters: typing.Optional[
        _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters
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
