import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_options_bacs_debit_mandate_options import (
    SetupIntentConfirmBodyPaymentMethodOptionsBacsDebitMandateOptions,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsBacsDebitMandateOptions,
)


class SetupIntentConfirmBodyPaymentMethodOptionsBacsDebit(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodOptionsBacsDebit
    """

    mandate_options: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsBacsDebitMandateOptions
    ]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptionsBacsDebit(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptionsBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsBacsDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
