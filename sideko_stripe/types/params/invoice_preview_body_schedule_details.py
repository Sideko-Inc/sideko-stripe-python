import pydantic
import typing
import typing_extensions

from .invoice_preview_body_schedule_details_phases_item import (
    InvoicePreviewBodyScheduleDetailsPhasesItem,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItem,
)


class InvoicePreviewBodyScheduleDetails(typing_extensions.TypedDict):
    """
    The schedule creation or modification params to apply as a preview. Cannot be used with `subscription` or `subscription_` prefixed fields.
    """

    end_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["cancel", "release"]
    ]

    phases: typing_extensions.NotRequired[
        typing.List[InvoicePreviewBodyScheduleDetailsPhasesItem]
    ]

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]


class _SerializerInvoicePreviewBodyScheduleDetails(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodyScheduleDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end_behavior: typing.Optional[typing_extensions.Literal["cancel", "release"]] = (
        pydantic.Field(alias="end_behavior", default=None)
    )
    phases: typing.Optional[
        typing.List[_SerializerInvoicePreviewBodyScheduleDetailsPhasesItem]
    ] = pydantic.Field(alias="phases", default=None)
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
