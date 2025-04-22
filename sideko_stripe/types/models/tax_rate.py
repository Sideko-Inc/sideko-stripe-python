import pydantic
import typing
import typing_extensions

from .tax_rate_flat_amount import TaxRateFlatAmount
from .tax_rate_metadata import TaxRateMetadata


class TaxRate(pydantic.BaseModel):
    """
    Tax rates can be applied to [invoices](/invoicing/taxes/tax-rates), [subscriptions](/billing/taxes/tax-rates) and [Checkout Sessions](/payments/checkout/use-manual-tax-rates) to collect tax.

    Related guide: [Tax rates](/billing/taxes/tax-rates)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Defaults to `true`. When set to `false`, this tax rate cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
    """
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    """
    The display name of the tax rates as it will appear to your customer on their receipt email, PDF, and the hosted invoice page.
    """
    effective_percentage: typing.Optional[float] = pydantic.Field(
        alias="effective_percentage", default=None
    )
    """
    Actual/effective tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true,
    this percentage reflects the rate actually used to calculate tax based on the product's taxability
    and whether the user is registered to collect taxes in the corresponding jurisdiction.
    """
    flat_amount: typing.Optional[TaxRateFlatAmount] = pydantic.Field(
        alias="flat_amount", default=None
    )
    """
    The amount of the tax rate when the `rate_type`` is `flat_amount`. Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    inclusive: bool = pydantic.Field(
        alias="inclusive",
    )
    """
    This specifies if the tax rate is inclusive or exclusive.
    """
    jurisdiction: typing.Optional[str] = pydantic.Field(
        alias="jurisdiction", default=None
    )
    """
    The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.
    """
    jurisdiction_level: typing.Optional[
        typing_extensions.Literal[
            "city", "country", "county", "district", "multiple", "state"
        ]
    ] = pydantic.Field(alias="jurisdiction_level", default=None)
    """
    The level of the jurisdiction that imposes this tax rate. Will be `null` for manually defined tax rates.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[TaxRateMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["tax_rate"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    percentage: float = pydantic.Field(
        alias="percentage",
    )
    """
    Tax rate percentage out of 100. For tax calculations with automatic_tax[enabled]=true, this percentage includes the statutory tax rate of non-taxable jurisdictions.
    """
    rate_type: typing.Optional[
        typing_extensions.Literal["flat_amount", "percentage"]
    ] = pydantic.Field(alias="rate_type", default=None)
    """
    Indicates the type of tax rate applied to the taxable amount. This value can be `null` when no tax applies to the location. This field is only present for TaxRates created by Stripe Tax.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, "NY" for New York, United States.
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
    The high-level tax type, such as `vat` or `sales_tax`.
    """
