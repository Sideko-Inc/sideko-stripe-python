import pydantic
import typing
import typing_extensions

from .invoice_preview_body_schedule_details_phases_item_add_invoice_items_item import (
    InvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItem,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItem,
)
from .invoice_preview_body_schedule_details_phases_item_automatic_tax import (
    InvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTax,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTax,
)
from .invoice_preview_body_schedule_details_phases_item_discounts_arr0_item import (
    InvoicePreviewBodyScheduleDetailsPhasesItemDiscountsArr0Item,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemDiscountsArr0Item,
)
from .invoice_preview_body_schedule_details_phases_item_invoice_settings import (
    InvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettings,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettings,
)
from .invoice_preview_body_schedule_details_phases_item_items_item import (
    InvoicePreviewBodyScheduleDetailsPhasesItemItemsItem,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItem,
)
from .invoice_preview_body_schedule_details_phases_item_metadata import (
    InvoicePreviewBodyScheduleDetailsPhasesItemMetadata,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemMetadata,
)
from .invoice_preview_body_schedule_details_phases_item_transfer_data import (
    InvoicePreviewBodyScheduleDetailsPhasesItemTransferData,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemTransferData,
)


class InvoicePreviewBodyScheduleDetailsPhasesItem(typing_extensions.TypedDict):
    """
    InvoicePreviewBodyScheduleDetailsPhasesItem
    """

    add_invoice_items: typing_extensions.NotRequired[
        typing.List[InvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItem]
    ]

    application_fee_percent: typing_extensions.NotRequired[float]

    automatic_tax: typing_extensions.NotRequired[
        InvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTax
    ]

    billing_cycle_anchor: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "phase_start"]
    ]

    collection_method: typing_extensions.NotRequired[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ]

    default_payment_method: typing_extensions.NotRequired[str]

    default_tax_rates: typing_extensions.NotRequired[
        typing.Union[typing.List[str], str]
    ]

    description: typing_extensions.NotRequired[typing.Union[str, str]]

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[InvoicePreviewBodyScheduleDetailsPhasesItemDiscountsArr0Item],
            str,
        ]
    ]

    end_date: typing_extensions.NotRequired[
        typing.Union[int, typing_extensions.Literal["now"]]
    ]

    invoice_settings: typing_extensions.NotRequired[
        InvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettings
    ]

    items: typing_extensions.Required[
        typing.List[InvoicePreviewBodyScheduleDetailsPhasesItemItemsItem]
    ]

    iterations: typing_extensions.NotRequired[int]

    metadata: typing_extensions.NotRequired[
        InvoicePreviewBodyScheduleDetailsPhasesItemMetadata
    ]

    on_behalf_of: typing_extensions.NotRequired[str]

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]

    start_date: typing_extensions.NotRequired[
        typing.Union[int, typing_extensions.Literal["now"]]
    ]

    transfer_data: typing_extensions.NotRequired[
        InvoicePreviewBodyScheduleDetailsPhasesItemTransferData
    ]

    trial: typing_extensions.NotRequired[bool]

    trial_end: typing_extensions.NotRequired[
        typing.Union[int, typing_extensions.Literal["now"]]
    ]


class _SerializerInvoicePreviewBodyScheduleDetailsPhasesItem(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodyScheduleDetailsPhasesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    add_invoice_items: typing.Optional[
        typing.List[
            _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItem
        ]
    ] = pydantic.Field(alias="add_invoice_items", default=None)
    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    automatic_tax: typing.Optional[
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTax
    ] = pydantic.Field(alias="automatic_tax", default=None)
    billing_cycle_anchor: typing.Optional[
        typing_extensions.Literal["automatic", "phase_start"]
    ] = pydantic.Field(alias="billing_cycle_anchor", default=None)
    collection_method: typing.Optional[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ] = pydantic.Field(alias="collection_method", default=None)
    default_payment_method: typing.Optional[str] = pydantic.Field(
        alias="default_payment_method", default=None
    )
    default_tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="default_tax_rates", default=None)
    )
    description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="description", default=None
    )
    discounts: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemDiscountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    end_date: typing.Optional[typing.Union[int, typing_extensions.Literal["now"]]] = (
        pydantic.Field(alias="end_date", default=None)
    )
    invoice_settings: typing.Optional[
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemInvoiceSettings
    ] = pydantic.Field(alias="invoice_settings", default=None)
    items: typing.List[
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItem
    ] = pydantic.Field(
        alias="items",
    )
    iterations: typing.Optional[int] = pydantic.Field(alias="iterations", default=None)
    metadata: typing.Optional[
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    start_date: typing.Optional[typing.Union[int, typing_extensions.Literal["now"]]] = (
        pydantic.Field(alias="start_date", default=None)
    )
    transfer_data: typing.Optional[
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemTransferData
    ] = pydantic.Field(alias="transfer_data", default=None)
    trial: typing.Optional[bool] = pydantic.Field(alias="trial", default=None)
    trial_end: typing.Optional[typing.Union[int, typing_extensions.Literal["now"]]] = (
        pydantic.Field(alias="trial_end", default=None)
    )
