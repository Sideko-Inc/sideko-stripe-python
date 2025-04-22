import pydantic
import typing_extensions

from .entitlements_feature_metadata import EntitlementsFeatureMetadata


class EntitlementsFeature(pydantic.BaseModel):
    """
    A feature represents a monetizable ability or functionality in your system.
    Features can be assigned to products, and when those products are purchased, Stripe will create an entitlement to the feature for the purchasing customer.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Inactive features cannot be attached to new products and will not be returned from the features list endpoint.
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
    lookup_key: str = pydantic.Field(
        alias="lookup_key",
    )
    """
    A unique key you provide as your own system identifier. This may be up to 80 characters.
    """
    metadata: EntitlementsFeatureMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The feature's name, for your own purpose, not meant to be displayable to the customer.
    """
    object: typing_extensions.Literal["entitlements.feature"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
