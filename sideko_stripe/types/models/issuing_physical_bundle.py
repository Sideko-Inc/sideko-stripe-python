import pydantic
import typing_extensions

from .issuing_physical_bundle_features import IssuingPhysicalBundleFeatures


class IssuingPhysicalBundle(pydantic.BaseModel):
    """
    A Physical Bundle represents the bundle of physical items - card stock, carrier letter, and envelope - that is shipped to a cardholder when you create a physical card.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    features: IssuingPhysicalBundleFeatures = pydantic.Field(
        alias="features",
    )
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
    name: str = pydantic.Field(
        alias="name",
    )
    """
    Friendly display name.
    """
    object: typing_extensions.Literal["issuing.physical_bundle"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["active", "inactive", "review"] = pydantic.Field(
        alias="status",
    )
    """
    Whether this physical bundle can be used to create cards.
    """
    type_: typing_extensions.Literal["custom", "standard"] = pydantic.Field(
        alias="type",
    )
    """
    Whether this physical bundle is a standard Stripe offering or custom-made for you.
    """
