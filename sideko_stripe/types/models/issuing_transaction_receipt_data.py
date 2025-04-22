import pydantic
import typing


class IssuingTransactionReceiptData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    The description of the item. The maximum length of this field is 26 characters.
    """
    quantity: typing.Optional[float] = pydantic.Field(alias="quantity", default=None)
    """
    The quantity of the item.
    """
    total: typing.Optional[int] = pydantic.Field(alias="total", default=None)
    """
    The total for this line item in cents.
    """
    unit_cost: typing.Optional[int] = pydantic.Field(alias="unit_cost", default=None)
    """
    The unit cost of the item in cents.
    """
