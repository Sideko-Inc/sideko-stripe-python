import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_line_items_item_price_data_product_data_metadata import (
    CheckoutSessionCreateBodyLineItemsItemPriceDataProductDataMetadata,
    _SerializerCheckoutSessionCreateBodyLineItemsItemPriceDataProductDataMetadata,
)


class CheckoutSessionCreateBodyLineItemsItemPriceDataProductData(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyLineItemsItemPriceDataProductData
    """

    description: typing_extensions.NotRequired[str]

    images: typing_extensions.NotRequired[typing.List[str]]

    metadata: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyLineItemsItemPriceDataProductDataMetadata
    ]

    name: typing_extensions.Required[str]

    tax_code: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyLineItemsItemPriceDataProductData(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyLineItemsItemPriceDataProductData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    images: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="images", default=None
    )
    metadata: typing.Optional[
        _SerializerCheckoutSessionCreateBodyLineItemsItemPriceDataProductDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
