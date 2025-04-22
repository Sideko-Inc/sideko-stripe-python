import pydantic
import typing


class DisputePaymentMethodDetailsPaypal(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    case_id: typing.Optional[str] = pydantic.Field(alias="case_id", default=None)
    """
    The ID of the dispute in PayPal.
    """
    reason_code: typing.Optional[str] = pydantic.Field(
        alias="reason_code", default=None
    )
    """
    The reason for the dispute as defined by PayPal
    """
