import pydantic
import typing
import typing_extensions

from .deleted_price import DeletedPrice
from .tax_rate import TaxRate

if typing_extensions.TYPE_CHECKING:
    from .discounts_resource_stackable_discount import (
        DiscountsResourceStackableDiscount,
    )
    from .price import Price


class SubscriptionScheduleAddInvoiceItem(pydantic.BaseModel):
    """
    An Add Invoice Item describes the prices and quantities that will be added as pending invoice items when entering a phase.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    discounts: typing.List["DiscountsResourceStackableDiscount"] = pydantic.Field(
        alias="discounts",
    )
    """
    The stackable discounts that will be applied to the item.
    """
    price: typing.Union[str, "Price", DeletedPrice] = pydantic.Field(
        alias="price",
    )
    """
    ID of the price used to generate the invoice item.
    """
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    """
    The quantity of the invoice item.
    """
    tax_rates: typing.Optional[typing.List[TaxRate]] = pydantic.Field(
        alias="tax_rates", default=None
    )
    """
    The tax rates which apply to the item. When set, the `default_tax_rates` do not apply to this item.
    """
