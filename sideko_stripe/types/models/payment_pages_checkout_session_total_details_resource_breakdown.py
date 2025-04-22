import pydantic
import typing
import typing_extensions

from .line_items_tax_amount import LineItemsTaxAmount

if typing_extensions.TYPE_CHECKING:
    from .line_items_discount_amount import LineItemsDiscountAmount


class PaymentPagesCheckoutSessionTotalDetailsResourceBreakdown(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    discounts: typing.List["LineItemsDiscountAmount"] = pydantic.Field(
        alias="discounts",
    )
    """
    The aggregated discounts.
    """
    taxes: typing.List[LineItemsTaxAmount] = pydantic.Field(
        alias="taxes",
    )
    """
    The aggregated tax amounts by rate.
    """
