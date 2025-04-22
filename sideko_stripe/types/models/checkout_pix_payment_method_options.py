import pydantic
import typing


class CheckoutPixPaymentMethodOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    expires_after_seconds: typing.Optional[int] = pydantic.Field(
        alias="expires_after_seconds", default=None
    )
    """
    The number of seconds after which Pix payment will expire.
    """
