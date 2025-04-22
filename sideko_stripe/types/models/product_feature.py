import pydantic
import typing_extensions

from .entitlements_feature import EntitlementsFeature


class ProductFeature(pydantic.BaseModel):
    """
    A product_feature represents an attachment between a feature and a product.
    When a product is purchased that has a feature attached, Stripe will create an entitlement to the feature for the purchasing customer.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    entitlement_feature: EntitlementsFeature = pydantic.Field(
        alias="entitlement_feature",
    )
    """
    A feature represents a monetizable ability or functionality in your system.
    Features can be assigned to products, and when those products are purchased, Stripe will create an entitlement to the feature for the purchasing customer.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["product_feature"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
