import pydantic
import typing


class IssuingAuthorizationFleetFuelPriceData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    gross_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="gross_amount_decimal", default=None
    )
    """
    Gross fuel amount that should equal Fuel Quantity multiplied by Fuel Unit Cost, inclusive of taxes.
    """
