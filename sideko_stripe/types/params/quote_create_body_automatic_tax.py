import pydantic
import typing
import typing_extensions

from .quote_create_body_automatic_tax_liability import (
    QuoteCreateBodyAutomaticTaxLiability,
    _SerializerQuoteCreateBodyAutomaticTaxLiability,
)


class QuoteCreateBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[QuoteCreateBodyAutomaticTaxLiability]


class _SerializerQuoteCreateBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for QuoteCreateBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[_SerializerQuoteCreateBodyAutomaticTaxLiability] = (
        pydantic.Field(alias="liability", default=None)
    )
