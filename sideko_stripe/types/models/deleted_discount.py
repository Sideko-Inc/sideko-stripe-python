import pydantic
import typing
import typing_extensions

from .coupon import Coupon
from .deleted_customer import DeletedCustomer

if typing_extensions.TYPE_CHECKING:
    from .customer import Customer
    from .promotion_code import PromotionCode


class DeletedDiscount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    checkout_session: typing.Optional[str] = pydantic.Field(
        alias="checkout_session", default=None
    )
    """
    The Checkout session that this coupon is applied to, if it is applied to a particular session in payment mode. Will not be present for subscription mode.
    """
    coupon: Coupon = pydantic.Field(
        alias="coupon",
    )
    """
    A coupon contains information about a percent-off or amount-off discount you
    might want to apply to a customer. Coupons may be applied to [subscriptions](https://stripe.com/docs/api#subscriptions), [invoices](https://stripe.com/docs/api#invoices),
    [checkout sessions](https://stripe.com/docs/api/checkout/sessions), [quotes](https://stripe.com/docs/api#quotes), and more. Coupons do not work with conventional one-off [charges](https://stripe.com/docs/api#create_charge) or [payment intents](https://stripe.com/docs/api/payment_intents).
    """
    customer: typing.Optional[typing.Union[str, "Customer", DeletedCustomer]] = (
        pydantic.Field(alias="customer", default=None)
    )
    """
    The ID of the customer associated with this discount.
    """
    deleted: bool = pydantic.Field(
        alias="deleted",
    )
    """
    Always true for a deleted object
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The ID of the discount object. Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to expand discount IDs in an array.
    """
    invoice: typing.Optional[str] = pydantic.Field(alias="invoice", default=None)
    """
    The invoice that the discount's coupon was applied to, if it was applied directly to a particular invoice.
    """
    invoice_item: typing.Optional[str] = pydantic.Field(
        alias="invoice_item", default=None
    )
    """
    The invoice item `id` (or invoice line item `id` for invoice line items of type='subscription') that the discount's coupon was applied to, if it was applied directly to a particular invoice item or invoice line item.
    """
    object: typing_extensions.Literal["discount"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    promotion_code: typing.Optional[typing.Union[str, "PromotionCode"]] = (
        pydantic.Field(alias="promotion_code", default=None)
    )
    """
    The promotion code applied to create this discount.
    """
    start: int = pydantic.Field(
        alias="start",
    )
    """
    Date that the coupon was applied.
    """
    subscription: typing.Optional[str] = pydantic.Field(
        alias="subscription", default=None
    )
    """
    The subscription that this coupon is applied to, if it is applied to a particular subscription.
    """
    subscription_item: typing.Optional[str] = pydantic.Field(
        alias="subscription_item", default=None
    )
    """
    The subscription item that this coupon is applied to, if it is applied to a particular subscription item.
    """
