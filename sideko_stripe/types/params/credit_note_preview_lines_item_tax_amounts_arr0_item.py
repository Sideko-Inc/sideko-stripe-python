import pydantic
import typing_extensions


class CreditNotePreviewLinesItemTaxAmountsArr0Item(typing_extensions.TypedDict):
    """
    CreditNotePreviewLinesItemTaxAmountsArr0Item
    """

    amount: typing_extensions.Required[int]

    tax_rate: typing_extensions.Required[str]

    taxable_amount: typing_extensions.Required[int]


class _SerializerCreditNotePreviewLinesItemTaxAmountsArr0Item(pydantic.BaseModel):
    """
    Serializer for CreditNotePreviewLinesItemTaxAmountsArr0Item handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    tax_rate: str = pydantic.Field(
        alias="tax_rate",
    )
    taxable_amount: int = pydantic.Field(
        alias="taxable_amount",
    )
