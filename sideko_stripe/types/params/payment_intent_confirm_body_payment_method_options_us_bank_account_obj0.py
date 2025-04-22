import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_us_bank_account_obj0_financial_connections import (
    PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnections,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnections,
)
from .payment_intent_confirm_body_payment_method_options_us_bank_account_obj0_mandate_options import (
    PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions,
)
from .payment_intent_confirm_body_payment_method_options_us_bank_account_obj0_networks import (
    PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0Networks,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0Networks,
)


class PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0
    """

    financial_connections: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnections
    ]

    mandate_options: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions
    ]

    networks: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0Networks
    ]

    preferred_settlement_speed: typing_extensions.NotRequired[
        typing_extensions.Literal["fastest", "standard"]
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    financial_connections: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnections
    ] = pydantic.Field(alias="financial_connections", default=None)
    mandate_options: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0MandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    networks: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsUsBankAccountObj0Networks
    ] = pydantic.Field(alias="networks", default=None)
    preferred_settlement_speed: typing.Optional[
        typing_extensions.Literal["fastest", "standard"]
    ] = pydantic.Field(alias="preferred_settlement_speed", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
