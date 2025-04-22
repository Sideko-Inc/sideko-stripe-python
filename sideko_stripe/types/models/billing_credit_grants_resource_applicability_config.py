import pydantic

from .billing_credit_grants_resource_scope import BillingCreditGrantsResourceScope


class BillingCreditGrantsResourceApplicabilityConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    scope: BillingCreditGrantsResourceScope = pydantic.Field(
        alias="scope",
    )
