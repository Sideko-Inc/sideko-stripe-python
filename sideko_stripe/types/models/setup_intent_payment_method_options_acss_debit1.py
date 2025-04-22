import pydantic
import typing
import typing_extensions

from .setup_intent_payment_method_options_mandate_options_acss_debit import (
    SetupIntentPaymentMethodOptionsMandateOptionsAcssDebit,
)


class SetupIntentPaymentMethodOptionsAcssDebit1(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    currency: typing.Optional[typing_extensions.Literal["cad", "usd"]] = pydantic.Field(
        alias="currency", default=None
    )
    """
    Currency supported by the bank account
    """
    mandate_options: typing.Optional[
        SetupIntentPaymentMethodOptionsMandateOptionsAcssDebit
    ] = pydantic.Field(alias="mandate_options", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
    """
    Bank account verification method.
    """
