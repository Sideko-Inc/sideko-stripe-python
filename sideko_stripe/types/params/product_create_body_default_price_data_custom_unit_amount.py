import pydantic
import typing
import typing_extensions


class ProductCreateBodyDefaultPriceDataCustomUnitAmount(typing_extensions.TypedDict):
    """
    ProductCreateBodyDefaultPriceDataCustomUnitAmount
    """

    enabled: typing_extensions.Required[bool]

    maximum: typing_extensions.NotRequired[int]

    minimum: typing_extensions.NotRequired[int]

    preset: typing_extensions.NotRequired[int]


class _SerializerProductCreateBodyDefaultPriceDataCustomUnitAmount(pydantic.BaseModel):
    """
    Serializer for ProductCreateBodyDefaultPriceDataCustomUnitAmount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    maximum: typing.Optional[int] = pydantic.Field(alias="maximum", default=None)
    minimum: typing.Optional[int] = pydantic.Field(alias="minimum", default=None)
    preset: typing.Optional[int] = pydantic.Field(alias="preset", default=None)
