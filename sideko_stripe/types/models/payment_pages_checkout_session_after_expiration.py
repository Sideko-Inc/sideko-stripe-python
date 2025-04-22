import pydantic
import typing

from .payment_pages_checkout_session_after_expiration_recovery import (
    PaymentPagesCheckoutSessionAfterExpirationRecovery,
)


class PaymentPagesCheckoutSessionAfterExpiration(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    recovery: typing.Optional[PaymentPagesCheckoutSessionAfterExpirationRecovery] = (
        pydantic.Field(alias="recovery", default=None)
    )
