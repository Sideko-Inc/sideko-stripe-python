import pydantic
import typing_extensions


class TaxProductResourceLineItemTaxRateDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    display_name: str = pydantic.Field(
        alias="display_name",
    )
    """
    A localized display name for tax type, intended to be human-readable. For example, "Local Sales and Use Tax", "Value-added tax (VAT)", or "Umsatzsteuer (USt.)".
    """
    percentage_decimal: str = pydantic.Field(
        alias="percentage_decimal",
    )
    """
    The tax rate percentage as a string. For example, 8.5% is represented as "8.5".
    """
    tax_type: typing_extensions.Literal[
        "amusement_tax",
        "communications_tax",
        "gst",
        "hst",
        "igst",
        "jct",
        "lease_tax",
        "pst",
        "qst",
        "retail_delivery_fee",
        "rst",
        "sales_tax",
        "service_tax",
        "vat",
    ] = pydantic.Field(
        alias="tax_type",
    )
    """
    The tax type, such as `vat` or `sales_tax`.
    """
