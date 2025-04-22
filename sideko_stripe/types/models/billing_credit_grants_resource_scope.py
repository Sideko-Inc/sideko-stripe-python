import pydantic
import typing
import typing_extensions

from .billing_credit_grants_resource_applicable_price import (
    BillingCreditGrantsResourceApplicablePrice,
)


class BillingCreditGrantsResourceScope(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    price_type: typing.Optional[typing_extensions.Literal["metered"]] = pydantic.Field(
        alias="price_type", default=None
    )
    """
    The price type that credit grants can apply to. We currently only support the `metered` price type. This refers to prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them. Cannot be used in combination with `prices`.
    """
    prices: typing.Optional[typing.List[BillingCreditGrantsResourceApplicablePrice]] = (
        pydantic.Field(alias="prices", default=None)
    )
    """
    The prices that credit grants can apply to. We currently only support `metered` prices. This refers to prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them. Cannot be used in combination with `price_type`.
    """
