import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyLineItemsItemPriceDataProductDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    CheckoutSessionCreateBodyLineItemsItemPriceDataProductDataMetadata
    """


class _SerializerCheckoutSessionCreateBodyLineItemsItemPriceDataProductDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyLineItemsItemPriceDataProductDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
