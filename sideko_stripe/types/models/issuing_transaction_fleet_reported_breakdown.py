import pydantic
import typing

from .issuing_transaction_fleet_fuel_price_data import (
    IssuingTransactionFleetFuelPriceData,
)
from .issuing_transaction_fleet_non_fuel_price_data import (
    IssuingTransactionFleetNonFuelPriceData,
)
from .issuing_transaction_fleet_tax_data import IssuingTransactionFleetTaxData


class IssuingTransactionFleetReportedBreakdown(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fuel: typing.Optional[IssuingTransactionFleetFuelPriceData] = pydantic.Field(
        alias="fuel", default=None
    )
    non_fuel: typing.Optional[IssuingTransactionFleetNonFuelPriceData] = pydantic.Field(
        alias="non_fuel", default=None
    )
    tax: typing.Optional[IssuingTransactionFleetTaxData] = pydantic.Field(
        alias="tax", default=None
    )
