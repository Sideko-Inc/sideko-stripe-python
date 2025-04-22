import pydantic
import typing


class IssuingTransactionFleetCardholderPromptData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    driver_id: typing.Optional[str] = pydantic.Field(alias="driver_id", default=None)
    """
    Driver ID.
    """
    odometer: typing.Optional[int] = pydantic.Field(alias="odometer", default=None)
    """
    Odometer reading.
    """
    unspecified_id: typing.Optional[str] = pydantic.Field(
        alias="unspecified_id", default=None
    )
    """
    An alphanumeric ID. This field is used when a vehicle ID, driver ID, or generic ID is entered by the cardholder, but the merchant or card network did not specify the prompt type.
    """
    user_id: typing.Optional[str] = pydantic.Field(alias="user_id", default=None)
    """
    User ID.
    """
    vehicle_number: typing.Optional[str] = pydantic.Field(
        alias="vehicle_number", default=None
    )
    """
    Vehicle number.
    """
