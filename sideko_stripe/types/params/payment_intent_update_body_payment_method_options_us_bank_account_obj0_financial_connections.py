import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_payment_method_options_us_bank_account_obj0_financial_connections_filters import (
    PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters,
)


class PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnections(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnections
    """

    filters: typing_extensions.NotRequired[
        PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters
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


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnections(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnections handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    filters: typing.Optional[
        _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters
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
