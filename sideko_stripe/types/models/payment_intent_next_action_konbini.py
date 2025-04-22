import pydantic
import typing

from .payment_intent_next_action_konbini_stores import (
    PaymentIntentNextActionKonbiniStores,
)


class PaymentIntentNextActionKonbini(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    expires_at: int = pydantic.Field(
        alias="expires_at",
    )
    """
    The timestamp at which the pending Konbini payment expires.
    """
    hosted_voucher_url: typing.Optional[str] = pydantic.Field(
        alias="hosted_voucher_url", default=None
    )
    """
    The URL for the Konbini payment instructions page, which allows customers to view and print a Konbini voucher.
    """
    stores: PaymentIntentNextActionKonbiniStores = pydantic.Field(
        alias="stores",
    )
