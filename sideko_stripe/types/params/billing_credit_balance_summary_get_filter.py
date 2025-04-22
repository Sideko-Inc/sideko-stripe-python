import pydantic
import typing
import typing_extensions

from .billing_credit_balance_summary_get_filter_applicability_scope import (
    BillingCreditBalanceSummaryGetFilterApplicabilityScope,
    _SerializerBillingCreditBalanceSummaryGetFilterApplicabilityScope,
)


class BillingCreditBalanceSummaryGetFilter(typing_extensions.TypedDict):
    """
    The filter criteria for the credit balance summary.
    """

    applicability_scope: typing_extensions.NotRequired[
        BillingCreditBalanceSummaryGetFilterApplicabilityScope
    ]

    credit_grant: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[
        typing_extensions.Literal["applicability_scope", "credit_grant"]
    ]


class _SerializerBillingCreditBalanceSummaryGetFilter(pydantic.BaseModel):
    """
    Serializer for BillingCreditBalanceSummaryGetFilter handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    applicability_scope: typing.Optional[
        _SerializerBillingCreditBalanceSummaryGetFilterApplicabilityScope
    ] = pydantic.Field(alias="applicability_scope", default=None)
    credit_grant: typing.Optional[str] = pydantic.Field(
        alias="credit_grant", default=None
    )
    type_: typing_extensions.Literal["applicability_scope", "credit_grant"] = (
        pydantic.Field(
            alias="type",
        )
    )
