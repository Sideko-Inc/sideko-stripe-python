import pydantic
import typing


class IssuingTransactionFlightDataLeg(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    arrival_airport_code: typing.Optional[str] = pydantic.Field(
        alias="arrival_airport_code", default=None
    )
    """
    The three-letter IATA airport code of the flight's destination.
    """
    carrier: typing.Optional[str] = pydantic.Field(alias="carrier", default=None)
    """
    The airline carrier code.
    """
    departure_airport_code: typing.Optional[str] = pydantic.Field(
        alias="departure_airport_code", default=None
    )
    """
    The three-letter IATA airport code that the flight departed from.
    """
    flight_number: typing.Optional[str] = pydantic.Field(
        alias="flight_number", default=None
    )
    """
    The flight number.
    """
    service_class: typing.Optional[str] = pydantic.Field(
        alias="service_class", default=None
    )
    """
    The flight's service class.
    """
    stopover_allowed: typing.Optional[bool] = pydantic.Field(
        alias="stopover_allowed", default=None
    )
    """
    Whether a stopover is allowed on this flight.
    """
