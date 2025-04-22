import pydantic
import typing
import typing_extensions


class SourceCreateBodySourceOrderItemsItem(typing_extensions.TypedDict):
    """
    SourceCreateBodySourceOrderItemsItem
    """

    amount: typing_extensions.NotRequired[int]

    currency: typing_extensions.NotRequired[str]

    description: typing_extensions.NotRequired[str]

    parent: typing_extensions.NotRequired[str]

    quantity: typing_extensions.NotRequired[int]

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["discount", "shipping", "sku", "tax"]
    ]


class _SerializerSourceCreateBodySourceOrderItemsItem(pydantic.BaseModel):
    """
    Serializer for SourceCreateBodySourceOrderItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    parent: typing.Optional[str] = pydantic.Field(alias="parent", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    type_: typing.Optional[
        typing_extensions.Literal["discount", "shipping", "sku", "tax"]
    ] = pydantic.Field(alias="type", default=None)
