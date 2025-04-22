import pydantic
import typing

from .issuing_authorization_fleet_fuel_price_data import (
    IssuingAuthorizationFleetFuelPriceData,
)
from .issuing_authorization_fleet_non_fuel_price_data import (
    IssuingAuthorizationFleetNonFuelPriceData,
)
from .issuing_authorization_fleet_tax_data import IssuingAuthorizationFleetTaxData


class IssuingAuthorizationFleetReportedBreakdown(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fuel: typing.Optional[IssuingAuthorizationFleetFuelPriceData] = pydantic.Field(
        alias="fuel", default=None
    )
    non_fuel: typing.Optional[IssuingAuthorizationFleetNonFuelPriceData] = (
        pydantic.Field(alias="non_fuel", default=None)
    )
    tax: typing.Optional[IssuingAuthorizationFleetTaxData] = pydantic.Field(
        alias="tax", default=None
    )
