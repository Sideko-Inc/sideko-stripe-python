import pydantic
import typing
import typing_extensions

from .invoice_preview_body_schedule_details_phases_item_automatic_tax_liability import (
    InvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTaxLiability,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTaxLiability,
)


class InvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTax(
    typing_extensions.TypedDict
):
    """
    InvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTax
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[
        InvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTaxLiability
    ]


class _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTax(
    pydantic.BaseModel
):
    """
    Serializer for InvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
