import pydantic

from .billing_credit_grants_resource_amount import BillingCreditGrantsResourceAmount


class CreditBalance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available_balance: BillingCreditGrantsResourceAmount = pydantic.Field(
        alias="available_balance",
    )
    ledger_balance: BillingCreditGrantsResourceAmount = pydantic.Field(
        alias="ledger_balance",
    )
