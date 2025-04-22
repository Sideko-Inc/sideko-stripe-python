import pydantic
import typing


class PaymentMethodDetailsAfterpayClearpay(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    order_id: typing.Optional[str] = pydantic.Field(alias="order_id", default=None)
    """
    The Afterpay order ID associated with this payment intent.
    """
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    Order identifier shown to the merchant in Afterpay’s online portal.
    """
