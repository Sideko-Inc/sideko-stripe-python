import pydantic
import typing


class IssuingAuthorizationFleetNonFuelPriceData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    gross_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="gross_amount_decimal", default=None
    )
    """
    Gross non-fuel amount that should equal the sum of the line items, inclusive of taxes.
    """
