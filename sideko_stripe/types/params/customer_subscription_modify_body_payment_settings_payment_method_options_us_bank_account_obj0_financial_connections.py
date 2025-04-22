import pydantic
import typing
import typing_extensions

from .customer_subscription_modify_body_payment_settings_payment_method_options_us_bank_account_obj0_financial_connections_filters import (
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters,
    _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters,
)


class CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections
    """

    filters: typing_extensions.NotRequired[
        CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters
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


class _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    filters: typing.Optional[
        _SerializerCustomerSubscriptionModifyBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters
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
