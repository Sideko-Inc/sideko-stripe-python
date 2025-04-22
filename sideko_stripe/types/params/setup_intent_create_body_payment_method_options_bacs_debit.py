import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_payment_method_options_bacs_debit_mandate_options import (
    SetupIntentCreateBodyPaymentMethodOptionsBacsDebitMandateOptions,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsBacsDebitMandateOptions,
)


class SetupIntentCreateBodyPaymentMethodOptionsBacsDebit(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodOptionsBacsDebit
    """

    mandate_options: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsBacsDebitMandateOptions
    ]


class _SerializerSetupIntentCreateBodyPaymentMethodOptionsBacsDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodOptionsBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsBacsDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
