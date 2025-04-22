import pydantic
import typing
import typing_extensions

from .tax_product_registrations_resource_country_options_eu_standard import (
    TaxProductRegistrationsResourceCountryOptionsEuStandard,
)


class TaxProductRegistrationsResourceCountryOptionsEurope(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    standard: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsEuStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
    """
    Type of registration in an EU country.
    """
