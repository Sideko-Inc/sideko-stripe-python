import pydantic
import typing
import typing_extensions

from .billing_credit_grants_resource_amount import BillingCreditGrantsResourceAmount

if typing_extensions.TYPE_CHECKING:
    from .billing_credit_grants_resource_balance_credits_applied import (
        BillingCreditGrantsResourceBalanceCreditsApplied,
    )


class BillingCreditGrantsResourceBalanceDebit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: BillingCreditGrantsResourceAmount = pydantic.Field(
        alias="amount",
    )
    credits_applied: typing.Optional[
        "BillingCreditGrantsResourceBalanceCreditsApplied"
    ] = pydantic.Field(alias="credits_applied", default=None)
    type_: typing_extensions.Literal[
        "credits_applied", "credits_expired", "credits_voided"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of debit transaction.
    """
