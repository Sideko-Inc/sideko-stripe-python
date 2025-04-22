import pydantic
import typing
import typing_extensions

from .invoice_preview_body_subscription_details_items_item_discounts_arr0_item import (
    InvoicePreviewBodySubscriptionDetailsItemsItemDiscountsArr0Item,
    _SerializerInvoicePreviewBodySubscriptionDetailsItemsItemDiscountsArr0Item,
)
from .invoice_preview_body_subscription_details_items_item_metadata_obj0 import (
    InvoicePreviewBodySubscriptionDetailsItemsItemMetadataObj0,
    _SerializerInvoicePreviewBodySubscriptionDetailsItemsItemMetadataObj0,
)
from .invoice_preview_body_subscription_details_items_item_price_data import (
    InvoicePreviewBodySubscriptionDetailsItemsItemPriceData,
    _SerializerInvoicePreviewBodySubscriptionDetailsItemsItemPriceData,
)


class InvoicePreviewBodySubscriptionDetailsItemsItem(typing_extensions.TypedDict):
    """
    InvoicePreviewBodySubscriptionDetailsItemsItem
    """

    clear_usage: typing_extensions.NotRequired[bool]

    deleted: typing_extensions.NotRequired[bool]

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                InvoicePreviewBodySubscriptionDetailsItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ]

    id: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        typing.Union[InvoicePreviewBodySubscriptionDetailsItemsItemMetadataObj0, str]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        InvoicePreviewBodySubscriptionDetailsItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerInvoicePreviewBodySubscriptionDetailsItemsItem(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodySubscriptionDetailsItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    clear_usage: typing.Optional[bool] = pydantic.Field(
        alias="clear_usage", default=None
    )
    deleted: typing.Optional[bool] = pydantic.Field(alias="deleted", default=None)
    discounts: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerInvoicePreviewBodySubscriptionDetailsItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    metadata: typing.Optional[
        typing.Union[
            _SerializerInvoicePreviewBodySubscriptionDetailsItemsItemMetadataObj0, str
        ]
    ] = pydantic.Field(alias="metadata", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerInvoicePreviewBodySubscriptionDetailsItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
