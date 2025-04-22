import pydantic
import typing
import typing_extensions

from .issuing_authorization_fleet_cardholder_prompt_data import (
    IssuingAuthorizationFleetCardholderPromptData,
)
from .issuing_authorization_fleet_reported_breakdown import (
    IssuingAuthorizationFleetReportedBreakdown,
)


class IssuingAuthorizationFleetData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cardholder_prompt_data: typing.Optional[
        IssuingAuthorizationFleetCardholderPromptData
    ] = pydantic.Field(alias="cardholder_prompt_data", default=None)
    purchase_type: typing.Optional[
        typing_extensions.Literal[
            "fuel_and_non_fuel_purchase", "fuel_purchase", "non_fuel_purchase"
        ]
    ] = pydantic.Field(alias="purchase_type", default=None)
    """
    The type of purchase.
    """
    reported_breakdown: typing.Optional[IssuingAuthorizationFleetReportedBreakdown] = (
        pydantic.Field(alias="reported_breakdown", default=None)
    )
    service_type: typing.Optional[
        typing_extensions.Literal[
            "full_service", "non_fuel_transaction", "self_service"
        ]
    ] = pydantic.Field(alias="service_type", default=None)
    """
    The type of fuel service.
    """
