import pydantic
import typing
import typing_extensions


class ProductFeatureCreateBody(typing_extensions.TypedDict, total=False):
    """
    ProductFeatureCreateBody
    """

    entitlement_feature: typing_extensions.Required[str]
    """
    The ID of the [Feature](https://stripe.com/docs/api/entitlements/feature) object attached to this product.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerProductFeatureCreateBody(pydantic.BaseModel):
    """
    Serializer for ProductFeatureCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    entitlement_feature: str = pydantic.Field(
        alias="entitlement_feature",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
