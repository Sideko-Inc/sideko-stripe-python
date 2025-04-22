import pydantic
import typing
import typing_extensions

from .tax_product_registrations_resource_country_options_us_local_amusement_tax import (
    TaxProductRegistrationsResourceCountryOptionsUsLocalAmusementTax,
)
from .tax_product_registrations_resource_country_options_us_local_lease_tax import (
    TaxProductRegistrationsResourceCountryOptionsUsLocalLeaseTax,
)
from .tax_product_registrations_resource_country_options_us_state_sales_tax import (
    TaxProductRegistrationsResourceCountryOptionsUsStateSalesTax,
)


class TaxProductRegistrationsResourceCountryOptionsUnitedStates(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    local_amusement_tax: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsUsLocalAmusementTax
    ] = pydantic.Field(alias="local_amusement_tax", default=None)
    local_lease_tax: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsUsLocalLeaseTax
    ] = pydantic.Field(alias="local_lease_tax", default=None)
    state: str = pydantic.Field(
        alias="state",
    )
    """
    Two-letter US state code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """
    state_sales_tax: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsUsStateSalesTax
    ] = pydantic.Field(alias="state_sales_tax", default=None)
    type_: typing_extensions.Literal[
        "local_amusement_tax",
        "local_lease_tax",
        "state_communications_tax",
        "state_retail_delivery_fee",
        "state_sales_tax",
    ] = pydantic.Field(
        alias="type",
    )
    """
    Type of registration in the US.
    """
