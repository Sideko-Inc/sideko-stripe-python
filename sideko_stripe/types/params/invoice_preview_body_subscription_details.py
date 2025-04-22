import pydantic
import typing
import typing_extensions

from .invoice_preview_body_subscription_details_items_item import (
    InvoicePreviewBodySubscriptionDetailsItemsItem,
    _SerializerInvoicePreviewBodySubscriptionDetailsItemsItem,
)


class InvoicePreviewBodySubscriptionDetails(typing_extensions.TypedDict):
    """
    The subscription creation or modification params to apply as a preview. Cannot be used with `schedule` or `schedule_details` fields.
    """

    billing_cycle_anchor: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["now", "unchanged"], int]
    ]

    cancel_at: typing_extensions.NotRequired[typing.Union[int, str]]

    cancel_at_period_end: typing_extensions.NotRequired[bool]

    cancel_now: typing_extensions.NotRequired[bool]

    default_tax_rates: typing_extensions.NotRequired[
        typing.Union[typing.List[str], str]
    ]

    items: typing_extensions.NotRequired[
        typing.List[InvoicePreviewBodySubscriptionDetailsItemsItem]
    ]

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]

    proration_date: typing_extensions.NotRequired[int]

    resume_at: typing_extensions.NotRequired[typing_extensions.Literal["now"]]

    start_date: typing_extensions.NotRequired[int]

    trial_end: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["now"], int]
    ]


class _SerializerInvoicePreviewBodySubscriptionDetails(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodySubscriptionDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    billing_cycle_anchor: typing.Optional[
        typing.Union[typing_extensions.Literal["now", "unchanged"], int]
    ] = pydantic.Field(alias="billing_cycle_anchor", default=None)
    cancel_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="cancel_at", default=None
    )
    cancel_at_period_end: typing.Optional[bool] = pydantic.Field(
        alias="cancel_at_period_end", default=None
    )
    cancel_now: typing.Optional[bool] = pydantic.Field(alias="cancel_now", default=None)
    default_tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="default_tax_rates", default=None)
    )
    items: typing.Optional[
        typing.List[_SerializerInvoicePreviewBodySubscriptionDetailsItemsItem]
    ] = pydantic.Field(alias="items", default=None)
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    proration_date: typing.Optional[int] = pydantic.Field(
        alias="proration_date", default=None
    )
    resume_at: typing.Optional[typing_extensions.Literal["now"]] = pydantic.Field(
        alias="resume_at", default=None
    )
    start_date: typing.Optional[int] = pydantic.Field(alias="start_date", default=None)
    trial_end: typing.Optional[typing.Union[typing_extensions.Literal["now"], int]] = (
        pydantic.Field(alias="trial_end", default=None)
    )
