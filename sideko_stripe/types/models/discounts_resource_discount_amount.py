import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .deleted_discount import DeletedDiscount
    from .discount import Discount


class DiscountsResourceDiscountAmount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount, in cents (or local equivalent), of the discount.
    """
    discount: typing.Union[str, "Discount", "DeletedDiscount"] = pydantic.Field(
        alias="discount",
    )
    """
    The discount that was applied to get this discount amount.
    """
