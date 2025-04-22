import pydantic
import typing
import typing_extensions

from .subscription_create_body_automatic_tax_liability import (
    SubscriptionCreateBodyAutomaticTaxLiability,
    _SerializerSubscriptionCreateBodyAutomaticTaxLiability,
)


class SubscriptionCreateBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[
        SubscriptionCreateBodyAutomaticTaxLiability
    ]


class _SerializerSubscriptionCreateBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for SubscriptionCreateBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerSubscriptionCreateBodyAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
