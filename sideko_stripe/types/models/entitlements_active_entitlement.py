import pydantic
import typing
import typing_extensions

from .entitlements_feature import EntitlementsFeature


class EntitlementsActiveEntitlement(pydantic.BaseModel):
    """
    An active entitlement describes access to a feature for a customer.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    feature: typing.Union[str, EntitlementsFeature] = pydantic.Field(
        alias="feature",
    )
    """
    The [Feature](https://stripe.com/docs/api/entitlements/feature) that the customer is entitled to.
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
    object: typing_extensions.Literal["entitlements.active_entitlement"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
