import pydantic
import typing

from .payment_pages_checkout_session_checkout_address_details import (
    PaymentPagesCheckoutSessionCheckoutAddressDetails,
)


class PaymentPagesCheckoutSessionCollectedInformation(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    shipping_details: typing.Optional[
        PaymentPagesCheckoutSessionCheckoutAddressDetails
    ] = pydantic.Field(alias="shipping_details", default=None)
