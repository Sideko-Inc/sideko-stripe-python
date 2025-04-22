import pydantic
import typing
import typing_extensions

from .quote_update_body_automatic_tax_liability import (
    QuoteUpdateBodyAutomaticTaxLiability,
    _SerializerQuoteUpdateBodyAutomaticTaxLiability,
)


class QuoteUpdateBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[QuoteUpdateBodyAutomaticTaxLiability]


class _SerializerQuoteUpdateBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for QuoteUpdateBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[_SerializerQuoteUpdateBodyAutomaticTaxLiability] = (
        pydantic.Field(alias="liability", default=None)
    )
