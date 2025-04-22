import pydantic
import typing

from .issuing_transaction_fleet_cardholder_prompt_data import (
    IssuingTransactionFleetCardholderPromptData,
)
from .issuing_transaction_fleet_reported_breakdown import (
    IssuingTransactionFleetReportedBreakdown,
)


class IssuingTransactionFleetData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cardholder_prompt_data: typing.Optional[
        IssuingTransactionFleetCardholderPromptData
    ] = pydantic.Field(alias="cardholder_prompt_data", default=None)
    purchase_type: typing.Optional[str] = pydantic.Field(
        alias="purchase_type", default=None
    )
    """
    The type of purchase. One of `fuel_purchase`, `non_fuel_purchase`, or `fuel_and_non_fuel_purchase`.
    """
    reported_breakdown: typing.Optional[IssuingTransactionFleetReportedBreakdown] = (
        pydantic.Field(alias="reported_breakdown", default=None)
    )
    service_type: typing.Optional[str] = pydantic.Field(
        alias="service_type", default=None
    )
    """
    The type of fuel service. One of `non_fuel_transaction`, `full_service`, or `self_service`.
    """
