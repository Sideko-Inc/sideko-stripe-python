import pydantic
import typing


class PaymentFlowsPrivatePaymentMethodsKlarnaDob(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    day: typing.Optional[int] = pydantic.Field(alias="day", default=None)
    """
    The day of birth, between 1 and 31.
    """
    month: typing.Optional[int] = pydantic.Field(alias="month", default=None)
    """
    The month of birth, between 1 and 12.
    """
    year: typing.Optional[int] = pydantic.Field(alias="year", default=None)
    """
    The four-digit year of birth.
    """
