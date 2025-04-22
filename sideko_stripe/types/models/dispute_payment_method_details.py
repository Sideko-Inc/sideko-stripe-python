import pydantic
import typing
import typing_extensions

from .dispute_payment_method_details_amazon_pay import (
    DisputePaymentMethodDetailsAmazonPay,
)
from .dispute_payment_method_details_card import DisputePaymentMethodDetailsCard
from .dispute_payment_method_details_klarna import DisputePaymentMethodDetailsKlarna
from .dispute_payment_method_details_paypal import DisputePaymentMethodDetailsPaypal


class DisputePaymentMethodDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amazon_pay: typing.Optional[DisputePaymentMethodDetailsAmazonPay] = pydantic.Field(
        alias="amazon_pay", default=None
    )
    card: typing.Optional[DisputePaymentMethodDetailsCard] = pydantic.Field(
        alias="card", default=None
    )
    klarna: typing.Optional[DisputePaymentMethodDetailsKlarna] = pydantic.Field(
        alias="klarna", default=None
    )
    paypal: typing.Optional[DisputePaymentMethodDetailsPaypal] = pydantic.Field(
        alias="paypal", default=None
    )
    type_: typing_extensions.Literal["amazon_pay", "card", "klarna", "paypal"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    Payment method type.
    """
