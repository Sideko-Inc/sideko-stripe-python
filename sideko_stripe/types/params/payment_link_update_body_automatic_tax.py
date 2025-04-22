import pydantic
import typing
import typing_extensions

from .payment_link_update_body_automatic_tax_liability import (
    PaymentLinkUpdateBodyAutomaticTaxLiability,
    _SerializerPaymentLinkUpdateBodyAutomaticTaxLiability,
)


class PaymentLinkUpdateBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Configuration for automatic tax collection.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[PaymentLinkUpdateBodyAutomaticTaxLiability]


class _SerializerPaymentLinkUpdateBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerPaymentLinkUpdateBodyAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
