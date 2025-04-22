import pydantic
import typing


class PortalSubscriptionUpdateProduct(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    prices: typing.List[str] = pydantic.Field(
        alias="prices",
    )
    """
    The list of price IDs which, when subscribed to, a subscription can be updated.
    """
    product: str = pydantic.Field(
        alias="product",
    )
    """
    The product ID.
    """
