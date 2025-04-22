import pydantic
import typing


class PaymentIntentNextActionKonbiniSeicomart(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    confirmation_number: typing.Optional[str] = pydantic.Field(
        alias="confirmation_number", default=None
    )
    """
    The confirmation number.
    """
    payment_code: str = pydantic.Field(
        alias="payment_code",
    )
    """
    The payment code.
    """
