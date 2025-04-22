import pydantic
import typing
import typing_extensions

from .tax_transaction_create_reversal_body_line_items_item_metadata import (
    TaxTransactionCreateReversalBodyLineItemsItemMetadata,
    _SerializerTaxTransactionCreateReversalBodyLineItemsItemMetadata,
)


class TaxTransactionCreateReversalBodyLineItemsItem(typing_extensions.TypedDict):
    """
    TaxTransactionCreateReversalBodyLineItemsItem
    """

    amount: typing_extensions.Required[int]

    amount_tax: typing_extensions.Required[int]

    metadata: typing_extensions.NotRequired[
        TaxTransactionCreateReversalBodyLineItemsItemMetadata
    ]

    original_line_item: typing_extensions.Required[str]

    quantity: typing_extensions.NotRequired[int]

    reference: typing_extensions.Required[str]


class _SerializerTaxTransactionCreateReversalBodyLineItemsItem(pydantic.BaseModel):
    """
    Serializer for TaxTransactionCreateReversalBodyLineItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    amount_tax: int = pydantic.Field(
        alias="amount_tax",
    )
    metadata: typing.Optional[
        _SerializerTaxTransactionCreateReversalBodyLineItemsItemMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    original_line_item: str = pydantic.Field(
        alias="original_line_item",
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    reference: str = pydantic.Field(
        alias="reference",
    )
