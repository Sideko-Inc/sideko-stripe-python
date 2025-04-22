import pydantic
import typing


class PriceTier(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    flat_amount: typing.Optional[int] = pydantic.Field(
        alias="flat_amount", default=None
    )
    """
    Price for the entire tier.
    """
    flat_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="flat_amount_decimal", default=None
    )
    """
    Same as `flat_amount`, but contains a decimal value with at most 12 decimal places.
    """
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    """
    Per unit price for units relevant to the tier.
    """
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
    """
    Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.
    """
    up_to: typing.Optional[int] = pydantic.Field(alias="up_to", default=None)
    """
    Up to and including to this quantity will be contained in the tier.
    """
