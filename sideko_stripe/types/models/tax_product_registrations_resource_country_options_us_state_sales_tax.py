import pydantic
import typing

from .tax_product_registrations_resource_country_options_us_state_sales_tax_election import (
    TaxProductRegistrationsResourceCountryOptionsUsStateSalesTaxElection,
)


class TaxProductRegistrationsResourceCountryOptionsUsStateSalesTax(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    elections: typing.Optional[
        typing.List[
            TaxProductRegistrationsResourceCountryOptionsUsStateSalesTaxElection
        ]
    ] = pydantic.Field(alias="elections", default=None)
    """
    Elections for the state sales tax registration.
    """
