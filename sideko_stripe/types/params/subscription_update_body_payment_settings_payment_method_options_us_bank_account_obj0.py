import pydantic
import typing
import typing_extensions

from .subscription_update_body_payment_settings_payment_method_options_us_bank_account_obj0_financial_connections import (
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections,
    _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections,
)


class SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0(
    typing_extensions.TypedDict
):
    """
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0
    """

    financial_connections: typing_extensions.NotRequired[
        SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections
    ]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    financial_connections: typing.Optional[
        _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections
    ] = pydantic.Field(alias="financial_connections", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
