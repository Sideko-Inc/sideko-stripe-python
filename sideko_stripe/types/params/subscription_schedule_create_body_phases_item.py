import pydantic
import typing
import typing_extensions

from .subscription_schedule_create_body_phases_item_add_invoice_items_item import (
    SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItem,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItem,
)
from .subscription_schedule_create_body_phases_item_automatic_tax import (
    SubscriptionScheduleCreateBodyPhasesItemAutomaticTax,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemAutomaticTax,
)
from .subscription_schedule_create_body_phases_item_discounts_arr0_item import (
    SubscriptionScheduleCreateBodyPhasesItemDiscountsArr0Item,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemDiscountsArr0Item,
)
from .subscription_schedule_create_body_phases_item_invoice_settings import (
    SubscriptionScheduleCreateBodyPhasesItemInvoiceSettings,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemInvoiceSettings,
)
from .subscription_schedule_create_body_phases_item_items_item import (
    SubscriptionScheduleCreateBodyPhasesItemItemsItem,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItem,
)
from .subscription_schedule_create_body_phases_item_metadata import (
    SubscriptionScheduleCreateBodyPhasesItemMetadata,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemMetadata,
)
from .subscription_schedule_create_body_phases_item_transfer_data import (
    SubscriptionScheduleCreateBodyPhasesItemTransferData,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemTransferData,
)


class SubscriptionScheduleCreateBodyPhasesItem(typing_extensions.TypedDict):
    """
    SubscriptionScheduleCreateBodyPhasesItem
    """

    add_invoice_items: typing_extensions.NotRequired[
        typing.List[SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItem]
    ]

    application_fee_percent: typing_extensions.NotRequired[float]

    automatic_tax: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyPhasesItemAutomaticTax
    ]

    billing_cycle_anchor: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "phase_start"]
    ]

    collection_method: typing_extensions.NotRequired[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ]

    currency: typing_extensions.NotRequired[str]

    default_payment_method: typing_extensions.NotRequired[str]

    default_tax_rates: typing_extensions.NotRequired[
        typing.Union[typing.List[str], str]
    ]

    description: typing_extensions.NotRequired[typing.Union[str, str]]

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[SubscriptionScheduleCreateBodyPhasesItemDiscountsArr0Item], str
        ]
    ]

    end_date: typing_extensions.NotRequired[int]

    invoice_settings: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyPhasesItemInvoiceSettings
    ]

    items: typing_extensions.Required[
        typing.List[SubscriptionScheduleCreateBodyPhasesItemItemsItem]
    ]

    iterations: typing_extensions.NotRequired[int]

    metadata: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyPhasesItemMetadata
    ]

    on_behalf_of: typing_extensions.NotRequired[str]

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]

    transfer_data: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyPhasesItemTransferData
    ]

    trial: typing_extensions.NotRequired[bool]

    trial_end: typing_extensions.NotRequired[int]


class _SerializerSubscriptionScheduleCreateBodyPhasesItem(pydantic.BaseModel):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    add_invoice_items: typing.Optional[
        typing.List[
            _SerializerSubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItem
        ]
    ] = pydantic.Field(alias="add_invoice_items", default=None)
    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    automatic_tax: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyPhasesItemAutomaticTax
    ] = pydantic.Field(alias="automatic_tax", default=None)
    billing_cycle_anchor: typing.Optional[
        typing_extensions.Literal["automatic", "phase_start"]
    ] = pydantic.Field(alias="billing_cycle_anchor", default=None)
    collection_method: typing.Optional[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ] = pydantic.Field(alias="collection_method", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
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
                _SerializerSubscriptionScheduleCreateBodyPhasesItemDiscountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    end_date: typing.Optional[int] = pydantic.Field(alias="end_date", default=None)
    invoice_settings: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyPhasesItemInvoiceSettings
    ] = pydantic.Field(alias="invoice_settings", default=None)
    items: typing.List[_SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItem] = (
        pydantic.Field(
            alias="items",
        )
    )
    iterations: typing.Optional[int] = pydantic.Field(alias="iterations", default=None)
    metadata: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyPhasesItemMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    transfer_data: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyPhasesItemTransferData
    ] = pydantic.Field(alias="transfer_data", default=None)
    trial: typing.Optional[bool] = pydantic.Field(alias="trial", default=None)
    trial_end: typing.Optional[int] = pydantic.Field(alias="trial_end", default=None)
