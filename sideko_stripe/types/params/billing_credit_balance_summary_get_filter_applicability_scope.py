import pydantic
import typing
import typing_extensions

from .billing_credit_balance_summary_get_filter_applicability_scope_prices_item import (
    BillingCreditBalanceSummaryGetFilterApplicabilityScopePricesItem,
    _SerializerBillingCreditBalanceSummaryGetFilterApplicabilityScopePricesItem,
)


class BillingCreditBalanceSummaryGetFilterApplicabilityScope(
    typing_extensions.TypedDict
):
    """
    BillingCreditBalanceSummaryGetFilterApplicabilityScope
    """

    price_type: typing_extensions.NotRequired[typing_extensions.Literal["metered"]]

    prices: typing_extensions.NotRequired[
        typing.List[BillingCreditBalanceSummaryGetFilterApplicabilityScopePricesItem]
    ]


class _SerializerBillingCreditBalanceSummaryGetFilterApplicabilityScope(
    pydantic.BaseModel
):
    """
    Serializer for BillingCreditBalanceSummaryGetFilterApplicabilityScope handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    price_type: typing.Optional[typing_extensions.Literal["metered"]] = pydantic.Field(
        alias="price_type", default=None
    )
    prices: typing.Optional[
        typing.List[
            _SerializerBillingCreditBalanceSummaryGetFilterApplicabilityScopePricesItem
        ]
    ] = pydantic.Field(alias="prices", default=None)
