import pydantic
import typing_extensions


class ShippingRateCurrencyOption(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    A non-negative integer in cents representing how much to charge.
    """
    tax_behavior: typing_extensions.Literal["exclusive", "inclusive", "unspecified"] = (
        pydantic.Field(
            alias="tax_behavior",
        )
    )
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """
