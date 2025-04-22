import pydantic
import typing
import typing_extensions

from .tax_transaction_create_reversal_body_line_items_item import (
    TaxTransactionCreateReversalBodyLineItemsItem,
    _SerializerTaxTransactionCreateReversalBodyLineItemsItem,
)
from .tax_transaction_create_reversal_body_metadata import (
    TaxTransactionCreateReversalBodyMetadata,
    _SerializerTaxTransactionCreateReversalBodyMetadata,
)
from .tax_transaction_create_reversal_body_shipping_cost import (
    TaxTransactionCreateReversalBodyShippingCost,
    _SerializerTaxTransactionCreateReversalBodyShippingCost,
)


class TaxTransactionCreateReversalBody(typing_extensions.TypedDict, total=False):
    """
    TaxTransactionCreateReversalBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    flat_amount: typing_extensions.NotRequired[int]
    """
    A flat amount to reverse across the entire transaction, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) in negative. This value represents the total amount to refund from the transaction, including taxes.
    """

    line_items: typing_extensions.NotRequired[
        typing.List[TaxTransactionCreateReversalBodyLineItemsItem]
    ]
    """
    The line item amounts to reverse.
    """

    metadata: typing_extensions.NotRequired[TaxTransactionCreateReversalBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    mode: typing_extensions.Required[typing_extensions.Literal["full", "partial"]]
    """
    If `partial`, the provided line item or shipping cost amounts are reversed. If `full`, the original transaction is fully reversed.
    """

    original_transaction: typing_extensions.Required[str]
    """
    The ID of the Transaction to partially or fully reverse.
    """

    reference: typing_extensions.Required[str]
    """
    A custom identifier for this reversal, such as `myOrder_123-refund_1`, which must be unique across all transactions. The reference helps identify this reversal transaction in exported [tax reports](https://stripe.com/docs/tax/reports).
    """

    shipping_cost: typing_extensions.NotRequired[
        TaxTransactionCreateReversalBodyShippingCost
    ]
    """
    The shipping cost to reverse.
    """


class _SerializerTaxTransactionCreateReversalBody(pydantic.BaseModel):
    """
    Serializer for TaxTransactionCreateReversalBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    flat_amount: typing.Optional[int] = pydantic.Field(
        alias="flat_amount", default=None
    )
    line_items: typing.Optional[
        typing.List[_SerializerTaxTransactionCreateReversalBodyLineItemsItem]
    ] = pydantic.Field(alias="line_items", default=None)
    metadata: typing.Optional[_SerializerTaxTransactionCreateReversalBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    mode: typing_extensions.Literal["full", "partial"] = pydantic.Field(
        alias="mode",
    )
    original_transaction: str = pydantic.Field(
        alias="original_transaction",
    )
    reference: str = pydantic.Field(
        alias="reference",
    )
    shipping_cost: typing.Optional[
        _SerializerTaxTransactionCreateReversalBodyShippingCost
    ] = pydantic.Field(alias="shipping_cost", default=None)
