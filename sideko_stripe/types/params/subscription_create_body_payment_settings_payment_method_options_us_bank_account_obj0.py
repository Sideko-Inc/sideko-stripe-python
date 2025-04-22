import pydantic
import typing
import typing_extensions

from .subscription_create_body_payment_settings_payment_method_options_us_bank_account_obj0_financial_connections import (
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections,
    _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections,
)


class SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0(
    typing_extensions.TypedDict
):
    """
    SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0
    """

    financial_connections: typing_extensions.NotRequired[
        SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections
    ]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    financial_connections: typing.Optional[
        _SerializerSubscriptionCreateBodyPaymentSettingsPaymentMethodOptionsUsBankAccountObj0FinancialConnections
    ] = pydantic.Field(alias="financial_connections", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
