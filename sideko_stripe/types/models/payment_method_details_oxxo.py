import pydantic
import typing


class PaymentMethodDetailsOxxo(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    """
    OXXO reference number
    """
