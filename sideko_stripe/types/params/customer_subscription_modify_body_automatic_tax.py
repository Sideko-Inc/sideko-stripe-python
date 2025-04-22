import pydantic
import typing
import typing_extensions

from .customer_subscription_modify_body_automatic_tax_liability import (
    CustomerSubscriptionModifyBodyAutomaticTaxLiability,
    _SerializerCustomerSubscriptionModifyBodyAutomaticTaxLiability,
)


class CustomerSubscriptionModifyBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[
        CustomerSubscriptionModifyBodyAutomaticTaxLiability
    ]


class _SerializerCustomerSubscriptionModifyBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionModifyBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerCustomerSubscriptionModifyBodyAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
