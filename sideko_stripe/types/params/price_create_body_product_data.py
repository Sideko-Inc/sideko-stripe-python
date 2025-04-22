import pydantic
import typing
import typing_extensions

from .price_create_body_product_data_metadata import (
    PriceCreateBodyProductDataMetadata,
    _SerializerPriceCreateBodyProductDataMetadata,
)


class PriceCreateBodyProductData(typing_extensions.TypedDict):
    """
    These fields can be used to create a new product that this price will belong to.
    """

    active: typing_extensions.NotRequired[bool]

    id: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[PriceCreateBodyProductDataMetadata]

    name: typing_extensions.Required[str]

    statement_descriptor: typing_extensions.NotRequired[str]

    tax_code: typing_extensions.NotRequired[str]

    unit_label: typing_extensions.NotRequired[str]


class _SerializerPriceCreateBodyProductData(pydantic.BaseModel):
    """
    Serializer for PriceCreateBodyProductData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    metadata: typing.Optional[_SerializerPriceCreateBodyProductDataMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    name: str = pydantic.Field(
        alias="name",
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
    unit_label: typing.Optional[str] = pydantic.Field(alias="unit_label", default=None)
