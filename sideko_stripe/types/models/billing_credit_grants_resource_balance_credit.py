import pydantic
import typing
import typing_extensions

from .billing_credit_grants_resource_amount import BillingCreditGrantsResourceAmount

if typing_extensions.TYPE_CHECKING:
    from .billing_credit_grants_resource_balance_credits_application_invoice_voided import (
        BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided,
    )


class BillingCreditGrantsResourceBalanceCredit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: BillingCreditGrantsResourceAmount = pydantic.Field(
        alias="amount",
    )
    credits_application_invoice_voided: typing.Optional[
        "BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided"
    ] = pydantic.Field(alias="credits_application_invoice_voided", default=None)
    type_: typing_extensions.Literal[
        "credits_application_invoice_voided", "credits_granted"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of credit transaction.
    """
