import pydantic
import typing
import typing_extensions

from .credit_note_preview1_lines_item_tax_amounts_arr0_item import (
    CreditNotePreview1LinesItemTaxAmountsArr0Item,
    _SerializerCreditNotePreview1LinesItemTaxAmountsArr0Item,
)


class CreditNotePreview1LinesItem(typing_extensions.TypedDict):
    """
    CreditNotePreview1LinesItem
    """

    amount: typing_extensions.NotRequired[int]

    description: typing_extensions.NotRequired[str]

    invoice_line_item: typing_extensions.NotRequired[str]

    quantity: typing_extensions.NotRequired[int]

    tax_amounts: typing_extensions.NotRequired[
        typing.Union[typing.List[CreditNotePreview1LinesItemTaxAmountsArr0Item], str]
    ]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    type_: typing_extensions.Required[
        typing_extensions.Literal["custom_line_item", "invoice_line_item"]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerCreditNotePreview1LinesItem(pydantic.BaseModel):
    """
    Serializer for CreditNotePreview1LinesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    invoice_line_item: typing.Optional[str] = pydantic.Field(
        alias="invoice_line_item", default=None
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_amounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerCreditNotePreview1LinesItemTaxAmountsArr0Item], str
        ]
    ] = pydantic.Field(alias="tax_amounts", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
    type_: typing_extensions.Literal["custom_line_item", "invoice_line_item"] = (
        pydantic.Field(
            alias="type",
        )
    )
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
