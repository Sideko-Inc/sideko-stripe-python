import pydantic
import typing
import typing_extensions

from .billing_credit_grants_resource_monetary_amount import (
    BillingCreditGrantsResourceMonetaryAmount,
)


class BillingCreditGrantsResourceAmount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    monetary: typing.Optional[BillingCreditGrantsResourceMonetaryAmount] = (
        pydantic.Field(alias="monetary", default=None)
    )
    type_: typing_extensions.Literal["monetary"] = pydantic.Field(
        alias="type",
    )
    """
    The type of this amount. We currently only support `monetary` billing credits.
    """
