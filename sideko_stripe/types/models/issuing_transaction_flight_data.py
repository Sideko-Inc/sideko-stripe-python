import pydantic
import typing

from .issuing_transaction_flight_data_leg import IssuingTransactionFlightDataLeg


class IssuingTransactionFlightData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    departure_at: typing.Optional[int] = pydantic.Field(
        alias="departure_at", default=None
    )
    """
    The time that the flight departed.
    """
    passenger_name: typing.Optional[str] = pydantic.Field(
        alias="passenger_name", default=None
    )
    """
    The name of the passenger.
    """
    refundable: typing.Optional[bool] = pydantic.Field(alias="refundable", default=None)
    """
    Whether the ticket is refundable.
    """
    segments: typing.Optional[typing.List[IssuingTransactionFlightDataLeg]] = (
        pydantic.Field(alias="segments", default=None)
    )
    """
    The legs of the trip.
    """
    travel_agency: typing.Optional[str] = pydantic.Field(
        alias="travel_agency", default=None
    )
    """
    The travel agency that issued the ticket.
    """
