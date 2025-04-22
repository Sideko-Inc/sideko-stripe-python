import pydantic
import typing
import typing_extensions


class PaymentLinkCreateBodyLineItemsItemAdjustableQuantity(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyLineItemsItemAdjustableQuantity
    """

    enabled: typing_extensions.Required[bool]

    maximum: typing_extensions.NotRequired[int]

    minimum: typing_extensions.NotRequired[int]


class _SerializerPaymentLinkCreateBodyLineItemsItemAdjustableQuantity(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkCreateBodyLineItemsItemAdjustableQuantity handling case conversions
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
