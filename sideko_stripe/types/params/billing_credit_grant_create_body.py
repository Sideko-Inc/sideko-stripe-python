import pydantic
import typing
import typing_extensions

from .billing_credit_grant_create_body_amount import (
    BillingCreditGrantCreateBodyAmount,
    _SerializerBillingCreditGrantCreateBodyAmount,
)
from .billing_credit_grant_create_body_applicability_config import (
    BillingCreditGrantCreateBodyApplicabilityConfig,
    _SerializerBillingCreditGrantCreateBodyApplicabilityConfig,
)
from .billing_credit_grant_create_body_metadata import (
    BillingCreditGrantCreateBodyMetadata,
    _SerializerBillingCreditGrantCreateBodyMetadata,
)


class BillingCreditGrantCreateBody(typing_extensions.TypedDict, total=False):
    """
    BillingCreditGrantCreateBody
    """

    amount: typing_extensions.Required[BillingCreditGrantCreateBodyAmount]
    """
    Amount of this credit grant.
    """

    applicability_config: typing_extensions.Required[
        BillingCreditGrantCreateBodyApplicabilityConfig
    ]
    """
    Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
    """

    category: typing_extensions.Required[
        typing_extensions.Literal["paid", "promotional"]
    ]
    """
    The category of this credit grant.
    """

    customer: typing_extensions.Required[str]
    """
    ID of the customer to receive the billing credits.
    """

    effective_at: typing_extensions.NotRequired[int]
    """
    The time when the billing credits become effective-when they're eligible for use. It defaults to the current timestamp if not specified.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[int]
    """
    The time when the billing credits expire. If not specified, the billing credits don't expire.
    """

    metadata: typing_extensions.NotRequired[BillingCreditGrantCreateBodyMetadata]
    """
    Set of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
    """

    name: typing_extensions.NotRequired[str]
    """
    A descriptive name shown in the Dashboard.
    """

    priority: typing_extensions.NotRequired[int]
    """
    The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.
    """


class _SerializerBillingCreditGrantCreateBody(pydantic.BaseModel):
    """
    Serializer for BillingCreditGrantCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: _SerializerBillingCreditGrantCreateBodyAmount = pydantic.Field(
        alias="amount",
    )
    applicability_config: _SerializerBillingCreditGrantCreateBodyApplicabilityConfig = (
        pydantic.Field(
            alias="applicability_config",
        )
    )
    category: typing_extensions.Literal["paid", "promotional"] = pydantic.Field(
        alias="category",
    )
    customer: str = pydantic.Field(
        alias="customer",
    )
    effective_at: typing.Optional[int] = pydantic.Field(
        alias="effective_at", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    metadata: typing.Optional[_SerializerBillingCreditGrantCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    priority: typing.Optional[int] = pydantic.Field(alias="priority", default=None)
