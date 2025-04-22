import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_options_sepa_debit_mandate_options import (
    SetupIntentConfirmBodyPaymentMethodOptionsSepaDebitMandateOptions,
    _SerializerSetupIntentConfirmBodyPaymentMethodOptionsSepaDebitMandateOptions,
)


class SetupIntentConfirmBodyPaymentMethodOptionsSepaDebit(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodOptionsSepaDebit
    """

    mandate_options: typing_extensions.NotRequired[
        SetupIntentConfirmBodyPaymentMethodOptionsSepaDebitMandateOptions
    ]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptionsSepaDebit(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptionsSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodOptionsSepaDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
