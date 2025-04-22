import pydantic
import typing

from .setup_intent_payment_method_options_mandate_options_bacs_debit import (
    SetupIntentPaymentMethodOptionsMandateOptionsBacsDebit,
)


class SetupIntentPaymentMethodOptionsBacsDebit1(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        SetupIntentPaymentMethodOptionsMandateOptionsBacsDebit
    ] = pydantic.Field(alias="mandate_options", default=None)
