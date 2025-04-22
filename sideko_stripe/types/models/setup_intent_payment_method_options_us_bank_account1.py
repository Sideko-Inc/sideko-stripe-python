import pydantic
import typing
import typing_extensions

from .linked_account_options_us_bank_account import LinkedAccountOptionsUsBankAccount
from .payment_method_options_us_bank_account_mandate_options import (
    PaymentMethodOptionsUsBankAccountMandateOptions,
)


class SetupIntentPaymentMethodOptionsUsBankAccount1(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    financial_connections: typing.Optional[LinkedAccountOptionsUsBankAccount] = (
        pydantic.Field(alias="financial_connections", default=None)
    )
    mandate_options: typing.Optional[
        PaymentMethodOptionsUsBankAccountMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
    """
    Bank account verification method.
    """
