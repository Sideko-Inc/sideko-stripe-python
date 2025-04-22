import pydantic
import typing


class DisputePaymentMethodDetailsKlarna(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reason_code: typing.Optional[str] = pydantic.Field(
        alias="reason_code", default=None
    )
    """
    The reason for the dispute as defined by Klarna
    """
