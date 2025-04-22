import pydantic
import typing

from .payment_links_resource_custom_text_position import (
    PaymentLinksResourceCustomTextPosition,
)


class PaymentLinksResourceCustomText(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    after_submit: typing.Optional[PaymentLinksResourceCustomTextPosition] = (
        pydantic.Field(alias="after_submit", default=None)
    )
    shipping_address: typing.Optional[PaymentLinksResourceCustomTextPosition] = (
        pydantic.Field(alias="shipping_address", default=None)
    )
    submit: typing.Optional[PaymentLinksResourceCustomTextPosition] = pydantic.Field(
        alias="submit", default=None
    )
    terms_of_service_acceptance: typing.Optional[
        PaymentLinksResourceCustomTextPosition
    ] = pydantic.Field(alias="terms_of_service_acceptance", default=None)
