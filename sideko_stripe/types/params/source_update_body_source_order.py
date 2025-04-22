import pydantic
import typing
import typing_extensions

from .source_update_body_source_order_items_item import (
    SourceUpdateBodySourceOrderItemsItem,
    _SerializerSourceUpdateBodySourceOrderItemsItem,
)
from .source_update_body_source_order_shipping import (
    SourceUpdateBodySourceOrderShipping,
    _SerializerSourceUpdateBodySourceOrderShipping,
)


class SourceUpdateBodySourceOrder(typing_extensions.TypedDict):
    """
    Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.
    """

    items: typing_extensions.NotRequired[
        typing.List[SourceUpdateBodySourceOrderItemsItem]
    ]

    shipping: typing_extensions.NotRequired[SourceUpdateBodySourceOrderShipping]


class _SerializerSourceUpdateBodySourceOrder(pydantic.BaseModel):
    """
    Serializer for SourceUpdateBodySourceOrder handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    items: typing.Optional[
        typing.List[_SerializerSourceUpdateBodySourceOrderItemsItem]
    ] = pydantic.Field(alias="items", default=None)
    shipping: typing.Optional[_SerializerSourceUpdateBodySourceOrderShipping] = (
        pydantic.Field(alias="shipping", default=None)
    )
