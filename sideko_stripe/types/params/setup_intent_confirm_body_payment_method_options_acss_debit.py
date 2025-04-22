import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_options_acss_debit_mandate_options import (
    SetupIntentConfirmBodyPaymentMethodOptionsAcssDebitMandateOptions,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsAcssDebitMandateOptions,
)


class SetupIntentConfirmBodyPaymentMethodOptionsAcssDebit(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodOptionsAcssDebit
    """

    currency: typing_extensions.NotRequired[typing_extensions.Literal["cad", "usd"]]

    mandate_options: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsAcssDebitMandateOptions
    ]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptionsAcssDebit(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptionsAcssDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency: typing.Optional[typing_extensions.Literal["cad", "usd"]] = pydantic.Field(
        alias="currency", default=None
    )
    mandate_options: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsAcssDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
