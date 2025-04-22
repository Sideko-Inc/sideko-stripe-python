import pydantic
import typing
import typing_extensions

from .tax_product_registrations_resource_country_options_ca_province_standard import (
    TaxProductRegistrationsResourceCountryOptionsCaProvinceStandard,
)


class TaxProductRegistrationsResourceCountryOptionsCanada(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    province_standard: typing.Optional[
        TaxProductRegistrationsResourceCountryOptionsCaProvinceStandard
    ] = pydantic.Field(alias="province_standard", default=None)
    type_: typing_extensions.Literal["province_standard", "simplified", "standard"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    Type of registration in Canada.
    """
