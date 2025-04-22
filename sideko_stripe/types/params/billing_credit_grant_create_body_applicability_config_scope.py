import pydantic
import typing
import typing_extensions

from .billing_credit_grant_create_body_applicability_config_scope_prices_item import (
    BillingCreditGrantCreateBodyApplicabilityConfigScopePricesItem,
    _SerializerBillingCreditGrantCreateBodyApplicabilityConfigScopePricesItem,
)


class BillingCreditGrantCreateBodyApplicabilityConfigScope(typing_extensions.TypedDict):
    """
    BillingCreditGrantCreateBodyApplicabilityConfigScope
    """

    price_type: typing_extensions.NotRequired[typing_extensions.Literal["metered"]]

    prices: typing_extensions.NotRequired[
        typing.List[BillingCreditGrantCreateBodyApplicabilityConfigScopePricesItem]
    ]


class _SerializerBillingCreditGrantCreateBodyApplicabilityConfigScope(
    pydantic.BaseModel
):
    """
    Serializer for BillingCreditGrantCreateBodyApplicabilityConfigScope handling case conversions
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
            _SerializerBillingCreditGrantCreateBodyApplicabilityConfigScopePricesItem
        ]
    ] = pydantic.Field(alias="prices", default=None)
