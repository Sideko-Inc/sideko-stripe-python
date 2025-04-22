import pydantic
import typing
import typing_extensions

from .tax_rate_flat_amount import TaxRateFlatAmount


class TaxProductResourceTaxRateDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    flat_amount: typing.Optional[TaxRateFlatAmount] = pydantic.Field(
        alias="flat_amount", default=None
    )
    """
    The amount of the tax rate when the `rate_type`` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.
    """
    percentage_decimal: str = pydantic.Field(
        alias="percentage_decimal",
    )
    """
    The tax rate percentage as a string. For example, 8.5% is represented as `"8.5"`.
    """
    rate_type: typing.Optional[
        typing_extensions.Literal["flat_amount", "percentage"]
    ] = pydantic.Field(alias="rate_type", default=None)
    """
    Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State, county, province, or region.
    """
    tax_type: typing.Optional[
        typing_extensions.Literal[
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
        ]
    ] = pydantic.Field(alias="tax_type", default=None)
    """
    The tax type, such as `vat` or `sales_tax`.
    """
