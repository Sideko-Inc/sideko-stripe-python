import pydantic
import typing
import typing_extensions

from .payment_method_details_passthrough_card import PaymentMethodDetailsPassthroughCard


class AmazonPayUnderlyingPaymentMethodFundingDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card: typing.Optional[PaymentMethodDetailsPassthroughCard] = pydantic.Field(
        alias="card", default=None
    )
    type_: typing.Optional[typing_extensions.Literal["card"]] = pydantic.Field(
        alias="type", default=None
    )
    """
    funding type of the underlying payment method.
    """
