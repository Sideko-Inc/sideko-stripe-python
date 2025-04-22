import pydantic
import typing
import typing_extensions

from .invoice_line_create_many_body_lines_item_tax_amounts_arr0_item_tax_rate_data import (
    InvoiceLineCreateManyBodyLinesItemTaxAmountsArr0ItemTaxRateData,
    _SerializerInvoiceLineCreateManyBodyLinesItemTaxAmountsArr0ItemTaxRateData,
)


class InvoiceLineCreateManyBodyLinesItemTaxAmountsArr0Item(typing_extensions.TypedDict):
    """
    InvoiceLineCreateManyBodyLinesItemTaxAmountsArr0Item
    """

    amount: typing_extensions.Required[int]

    tax_rate_data: typing_extensions.Required[
        InvoiceLineCreateManyBodyLinesItemTaxAmountsArr0ItemTaxRateData
    ]

    taxability_reason: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "customer_exempt",
            "not_collecting",
            "not_subject_to_tax",
            "not_supported",
            "portion_product_exempt",
            "portion_reduced_rated",
            "portion_standard_rated",
            "product_exempt",
            "product_exempt_holiday",
            "proportionally_rated",
            "reduced_rated",
            "reverse_charge",
            "standard_rated",
            "taxable_basis_reduced",
            "zero_rated",
        ]
    ]

    taxable_amount: typing_extensions.Required[int]


class _SerializerInvoiceLineCreateManyBodyLinesItemTaxAmountsArr0Item(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceLineCreateManyBodyLinesItemTaxAmountsArr0Item handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    tax_rate_data: _SerializerInvoiceLineCreateManyBodyLinesItemTaxAmountsArr0ItemTaxRateData = pydantic.Field(
        alias="tax_rate_data",
    )
    taxability_reason: typing.Optional[
        typing_extensions.Literal[
            "customer_exempt",
            "not_collecting",
            "not_subject_to_tax",
            "not_supported",
            "portion_product_exempt",
            "portion_reduced_rated",
            "portion_standard_rated",
            "product_exempt",
            "product_exempt_holiday",
            "proportionally_rated",
            "reduced_rated",
            "reverse_charge",
            "standard_rated",
            "taxable_basis_reduced",
            "zero_rated",
        ]
    ] = pydantic.Field(alias="taxability_reason", default=None)
    taxable_amount: int = pydantic.Field(
        alias="taxable_amount",
    )
