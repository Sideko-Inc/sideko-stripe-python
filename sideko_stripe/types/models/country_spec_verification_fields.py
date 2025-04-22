import pydantic

from .country_spec_verification_field_details import CountrySpecVerificationFieldDetails


class CountrySpecVerificationFields(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    company: CountrySpecVerificationFieldDetails = pydantic.Field(
        alias="company",
    )
    individual: CountrySpecVerificationFieldDetails = pydantic.Field(
        alias="individual",
    )
