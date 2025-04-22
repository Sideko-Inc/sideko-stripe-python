import pydantic
import typing
import typing_extensions

from .source_create_body_source_order_items_item import (
    SourceCreateBodySourceOrderItemsItem,
    _SerializerSourceCreateBodySourceOrderItemsItem,
)
from .source_create_body_source_order_shipping import (
    SourceCreateBodySourceOrderShipping,
    _SerializerSourceCreateBodySourceOrderShipping,
)


class SourceCreateBodySourceOrder(typing_extensions.TypedDict):
    """
    Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.
    """

    items: typing_extensions.NotRequired[
        typing.List[SourceCreateBodySourceOrderItemsItem]
    ]

    shipping: typing_extensions.NotRequired[SourceCreateBodySourceOrderShipping]


class _SerializerSourceCreateBodySourceOrder(pydantic.BaseModel):
    """
    Serializer for SourceCreateBodySourceOrder handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    items: typing.Optional[
        typing.List[_SerializerSourceCreateBodySourceOrderItemsItem]
    ] = pydantic.Field(alias="items", default=None)
    shipping: typing.Optional[_SerializerSourceCreateBodySourceOrderShipping] = (
        pydantic.Field(alias="shipping", default=None)
    )
