import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyLineItemsItemAdjustableQuantity(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyLineItemsItemAdjustableQuantity
    """

    enabled: typing_extensions.Required[bool]

    maximum: typing_extensions.NotRequired[int]

    minimum: typing_extensions.NotRequired[int]


class _SerializerCheckoutSessionCreateBodyLineItemsItemAdjustableQuantity(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyLineItemsItemAdjustableQuantity handling case conversions
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
