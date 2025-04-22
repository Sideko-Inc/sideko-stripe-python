import pydantic
import typing
import typing_extensions

from .tax_product_resource_customer_details import TaxProductResourceCustomerDetails
from .tax_product_resource_ship_from_details import TaxProductResourceShipFromDetails
from .tax_product_resource_tax_transaction_resource_reversal import (
    TaxProductResourceTaxTransactionResourceReversal,
)
from .tax_product_resource_tax_transaction_shipping_cost import (
    TaxProductResourceTaxTransactionShippingCost,
)
from .tax_transaction_line_items import TaxTransactionLineItems
from .tax_transaction_metadata import TaxTransactionMetadata


class TaxTransaction(pydantic.BaseModel):
    """
    A Tax Transaction records the tax collected from or refunded to your customer.

    Related guide: [Calculate tax in your custom payment flow](https://stripe.com/docs/tax/custom#tax-transaction)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    """
    The ID of an existing [Customer](https://stripe.com/docs/api/customers/object) used for the resource.
    """
    customer_details: TaxProductResourceCustomerDetails = pydantic.Field(
        alias="customer_details",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the transaction.
    """
    line_items: typing.Optional[TaxTransactionLineItems] = pydantic.Field(
        alias="line_items", default=None
    )
    """
    The tax collected or refunded, by line item.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[TaxTransactionMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["tax.transaction"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    posted_at: int = pydantic.Field(
        alias="posted_at",
    )
    """
    The Unix timestamp representing when the tax liability is assumed or reduced.
    """
    reference: str = pydantic.Field(
        alias="reference",
    )
    """
    A custom unique identifier, such as 'myOrder_123'.
    """
    reversal: typing.Optional[TaxProductResourceTaxTransactionResourceReversal] = (
        pydantic.Field(alias="reversal", default=None)
    )
    ship_from_details: typing.Optional[TaxProductResourceShipFromDetails] = (
        pydantic.Field(alias="ship_from_details", default=None)
    )
    shipping_cost: typing.Optional[TaxProductResourceTaxTransactionShippingCost] = (
        pydantic.Field(alias="shipping_cost", default=None)
    )
    tax_date: int = pydantic.Field(
        alias="tax_date",
    )
    """
    Timestamp of date at which the tax rules and rates in effect applies for the calculation.
    """
    type_: typing_extensions.Literal["reversal", "transaction"] = pydantic.Field(
        alias="type",
    )
    """
    If `reversal`, this transaction reverses an earlier transaction.
    """
