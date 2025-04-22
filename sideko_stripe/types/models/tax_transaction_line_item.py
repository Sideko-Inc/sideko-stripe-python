import pydantic
import typing
import typing_extensions

from .tax_product_resource_tax_transaction_line_item_resource_reversal import (
    TaxProductResourceTaxTransactionLineItemResourceReversal,
)
from .tax_transaction_line_item_metadata import TaxTransactionLineItemMetadata


class TaxTransactionLineItem(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The line item amount in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If `tax_behavior=inclusive`, then this amount includes taxes. Otherwise, taxes were calculated on top of this amount.
    """
    amount_tax: int = pydantic.Field(
        alias="amount_tax",
    )
    """
    The amount of tax calculated for this line item, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[TaxTransactionLineItemMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["tax.transaction_line_item"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    product: typing.Optional[str] = pydantic.Field(alias="product", default=None)
    """
    The ID of an existing [Product](https://stripe.com/docs/api/products/object).
    """
    quantity: int = pydantic.Field(
        alias="quantity",
    )
    """
    The number of units of the item being purchased. For reversals, this is the quantity reversed.
    """
    reference: str = pydantic.Field(
        alias="reference",
    )
    """
    A custom identifier for this line item in the transaction.
    """
    reversal: typing.Optional[
        TaxProductResourceTaxTransactionLineItemResourceReversal
    ] = pydantic.Field(alias="reversal", default=None)
    tax_behavior: typing_extensions.Literal["exclusive", "inclusive"] = pydantic.Field(
        alias="tax_behavior",
    )
    """
    Specifies whether the `amount` includes taxes. If `tax_behavior=inclusive`, then the amount includes taxes.
    """
    tax_code: str = pydantic.Field(
        alias="tax_code",
    )
    """
    The [tax code](https://stripe.com/docs/tax/tax-categories) ID used for this resource.
    """
    type_: typing_extensions.Literal["reversal", "transaction"] = pydantic.Field(
        alias="type",
    )
    """
    If `reversal`, this line item reverses an earlier transaction.
    """
