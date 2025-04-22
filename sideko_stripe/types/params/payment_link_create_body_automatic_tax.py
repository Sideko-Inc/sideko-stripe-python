import pydantic
import typing
import typing_extensions

from .payment_link_create_body_automatic_tax_liability import (
    PaymentLinkCreateBodyAutomaticTaxLiability,
    _SerializerPaymentLinkCreateBodyAutomaticTaxLiability,
)


class PaymentLinkCreateBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Configuration for automatic tax collection.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[PaymentLinkCreateBodyAutomaticTaxLiability]


class _SerializerPaymentLinkCreateBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerPaymentLinkCreateBodyAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
