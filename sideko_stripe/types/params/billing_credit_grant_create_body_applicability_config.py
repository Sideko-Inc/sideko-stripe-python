import pydantic
import typing_extensions

from .billing_credit_grant_create_body_applicability_config_scope import (
    BillingCreditGrantCreateBodyApplicabilityConfigScope,
    _SerializerBillingCreditGrantCreateBodyApplicabilityConfigScope,
)


class BillingCreditGrantCreateBodyApplicabilityConfig(typing_extensions.TypedDict):
    """
    Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
    """

    scope: typing_extensions.Required[
        BillingCreditGrantCreateBodyApplicabilityConfigScope
    ]


class _SerializerBillingCreditGrantCreateBodyApplicabilityConfig(pydantic.BaseModel):
    """
    Serializer for BillingCreditGrantCreateBodyApplicabilityConfig handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    scope: _SerializerBillingCreditGrantCreateBodyApplicabilityConfigScope = (
        pydantic.Field(
            alias="scope",
        )
    )
