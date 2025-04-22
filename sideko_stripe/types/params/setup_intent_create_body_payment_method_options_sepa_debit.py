import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_payment_method_options_sepa_debit_mandate_options import (
    SetupIntentCreateBodyPaymentMethodOptionsSepaDebitMandateOptions,
    _SerializerSetupIntentCreateBodyPaymentMethodOptionsSepaDebitMandateOptions,
)


class SetupIntentCreateBodyPaymentMethodOptionsSepaDebit(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodOptionsSepaDebit
    """

    mandate_options: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptionsSepaDebitMandateOptions
    ]


class _SerializerSetupIntentCreateBodyPaymentMethodOptionsSepaDebit(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodOptionsSepaDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptionsSepaDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
