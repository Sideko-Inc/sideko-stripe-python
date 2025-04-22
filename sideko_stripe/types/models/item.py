import pydantic
import typing
import typing_extensions

from .line_items_tax_amount import LineItemsTaxAmount

if typing_extensions.TYPE_CHECKING:
    from .line_items_discount_amount import LineItemsDiscountAmount
    from .price import Price


class Item(pydantic.BaseModel):
    """
    A line item.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_discount: int = pydantic.Field(
        alias="amount_discount",
    )
    """
    Total discount amount applied. If no discounts were applied, defaults to 0.
    """
    amount_subtotal: int = pydantic.Field(
        alias="amount_subtotal",
    )
    """
    Total before any discounts or taxes are applied.
    """
    amount_tax: int = pydantic.Field(
        alias="amount_tax",
    )
    """
    Total tax amount applied. If no tax was applied, defaults to 0.
    """
    amount_total: int = pydantic.Field(
        alias="amount_total",
    )
    """
    Total after discounts and taxes.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users. Defaults to product name.
    """
    discounts: typing.Optional[typing.List["LineItemsDiscountAmount"]] = pydantic.Field(
        alias="discounts", default=None
    )
    """
    The discounts applied to the line item.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    object: typing_extensions.Literal["item"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    price: typing.Optional["Price"] = pydantic.Field(alias="price", default=None)
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.
    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.
    
    For example, you might have a single "gold" product that has prices for $10/month, $100/year, and €9 once.
    
    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription), [create an invoice](https://stripe.com/docs/billing/invoices/create), and more about [products and prices](https://stripe.com/docs/products-prices/overview).
    """
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    """
    The quantity of products being purchased.
    """
    taxes: typing.Optional[typing.List[LineItemsTaxAmount]] = pydantic.Field(
        alias="taxes", default=None
    )
    """
    The taxes applied to the line item.
    """
