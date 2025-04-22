import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_options_bacs_debit_mandate_options import (
    SetupIntentUpdateBodyPaymentMethodOptionsBacsDebitMandateOptions,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsBacsDebitMandateOptions,
)


class SetupIntentUpdateBodyPaymentMethodOptionsBacsDebit(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsBacsDebit
    """

    mandate_options: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsBacsDebitMandateOptions
    ]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsBacsDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsBacsDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
