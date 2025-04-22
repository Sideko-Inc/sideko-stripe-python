import pydantic
import typing
import typing_extensions

from .customer_subscription_create_body_automatic_tax_liability import (
    CustomerSubscriptionCreateBodyAutomaticTaxLiability,
    _SerializerCustomerSubscriptionCreateBodyAutomaticTaxLiability,
)


class CustomerSubscriptionCreateBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyAutomaticTaxLiability
    ]


class _SerializerCustomerSubscriptionCreateBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionCreateBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
