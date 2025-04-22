import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_options_sepa_debit_mandate_options import (
    SetupIntentUpdateBodyPaymentMethodOptionsSepaDebitMandateOptions,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptionsSepaDebitMandateOptions,
)


class SetupIntentUpdateBodyPaymentMethodOptionsSepaDebit(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsSepaDebit
    """

    mandate_options: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptionsSepaDebitMandateOptions
    ]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsSepaDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptionsSepaDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
