import pydantic
import typing_extensions


class TaxDeductedAtSource(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    object: typing_extensions.Literal["tax_deducted_at_source"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    period_end: int = pydantic.Field(
        alias="period_end",
    )
    """
    The end of the invoicing period. This TDS applies to Stripe fees collected during this invoicing period.
    """
    period_start: int = pydantic.Field(
        alias="period_start",
    )
    """
    The start of the invoicing period. This TDS applies to Stripe fees collected during this invoicing period.
    """
    tax_deduction_account_number: str = pydantic.Field(
        alias="tax_deduction_account_number",
    )
    """
    The TAN that was supplied to Stripe when TDS was assessed
    """
