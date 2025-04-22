import pydantic
import typing
import typing_extensions

from .billing_credit_grant_metadata import BillingCreditGrantMetadata
from .billing_credit_grants_resource_amount import BillingCreditGrantsResourceAmount
from .billing_credit_grants_resource_applicability_config import (
    BillingCreditGrantsResourceApplicabilityConfig,
)
from .deleted_customer import DeletedCustomer
from .test_helpers_test_clock import TestHelpersTestClock

if typing_extensions.TYPE_CHECKING:
    from .customer import Customer


class BillingCreditGrant(pydantic.BaseModel):
    """
    A credit grant is an API resource that documents the allocation of some billing credits to a customer.

    Related guide: [Billing credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: BillingCreditGrantsResourceAmount = pydantic.Field(
        alias="amount",
    )
    applicability_config: BillingCreditGrantsResourceApplicabilityConfig = (
        pydantic.Field(
            alias="applicability_config",
        )
    )
    category: typing_extensions.Literal["paid", "promotional"] = pydantic.Field(
        alias="category",
    )
    """
    The category of this credit grant. This is for tracking purposes and isn't displayed to the customer.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: typing.Union[str, "Customer", DeletedCustomer] = pydantic.Field(
        alias="customer",
    )
    """
    ID of the customer receiving the billing credits.
    """
    effective_at: typing.Optional[int] = pydantic.Field(
        alias="effective_at", default=None
    )
    """
    The time when the billing credits become effective-when they're eligible for use.
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    The time when the billing credits expire. If not present, the billing credits don't expire.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: BillingCreditGrantMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    A descriptive name shown in dashboard.
    """
    object: typing_extensions.Literal["billing.credit_grant"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    priority: typing.Optional[int] = pydantic.Field(alias="priority", default=None)
    """
    The priority for applying this credit grant. The highest priority is 0 and the lowest is 100.
    """
    test_clock: typing.Optional[typing.Union[str, TestHelpersTestClock]] = (
        pydantic.Field(alias="test_clock", default=None)
    )
    """
    ID of the test clock this credit grant belongs to.
    """
    updated: int = pydantic.Field(
        alias="updated",
    )
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """
    voided_at: typing.Optional[int] = pydantic.Field(alias="voided_at", default=None)
    """
    The time when this credit grant was voided. If not present, the credit grant hasn't been voided.
    """
