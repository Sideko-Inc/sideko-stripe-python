import pydantic
import typing

from .issuing_transaction_fleet_data import IssuingTransactionFleetData
from .issuing_transaction_flight_data import IssuingTransactionFlightData
from .issuing_transaction_fuel_data import IssuingTransactionFuelData
from .issuing_transaction_lodging_data import IssuingTransactionLodgingData
from .issuing_transaction_receipt_data import IssuingTransactionReceiptData


class IssuingTransactionPurchaseDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fleet: typing.Optional[IssuingTransactionFleetData] = pydantic.Field(
        alias="fleet", default=None
    )
    flight: typing.Optional[IssuingTransactionFlightData] = pydantic.Field(
        alias="flight", default=None
    )
    fuel: typing.Optional[IssuingTransactionFuelData] = pydantic.Field(
        alias="fuel", default=None
    )
    lodging: typing.Optional[IssuingTransactionLodgingData] = pydantic.Field(
        alias="lodging", default=None
    )
    receipt: typing.Optional[typing.List[IssuingTransactionReceiptData]] = (
        pydantic.Field(alias="receipt", default=None)
    )
    """
    The line items in the purchase.
    """
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    A merchant-specific order number.
    """
