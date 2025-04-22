import pydantic
import typing

from .payment_pages_checkout_session_custom_text_position import (
    PaymentPagesCheckoutSessionCustomTextPosition,
)


class PaymentPagesCheckoutSessionCustomText(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    after_submit: typing.Optional[PaymentPagesCheckoutSessionCustomTextPosition] = (
        pydantic.Field(alias="after_submit", default=None)
    )
    shipping_address: typing.Optional[PaymentPagesCheckoutSessionCustomTextPosition] = (
        pydantic.Field(alias="shipping_address", default=None)
    )
    submit: typing.Optional[PaymentPagesCheckoutSessionCustomTextPosition] = (
        pydantic.Field(alias="submit", default=None)
    )
    terms_of_service_acceptance: typing.Optional[
        PaymentPagesCheckoutSessionCustomTextPosition
    ] = pydantic.Field(alias="terms_of_service_acceptance", default=None)
