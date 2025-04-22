import pydantic
import typing

from .shipping_rate import ShippingRate


class PaymentLinksResourceShippingOption(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    shipping_amount: int = pydantic.Field(
        alias="shipping_amount",
    )
    """
    A non-negative integer in cents representing how much to charge.
    """
    shipping_rate: typing.Union[str, ShippingRate] = pydantic.Field(
        alias="shipping_rate",
    )
    """
    The ID of the Shipping Rate to use for this shipping option.
    """
