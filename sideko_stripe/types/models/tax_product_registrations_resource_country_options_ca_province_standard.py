import pydantic


class TaxProductRegistrationsResourceCountryOptionsCaProvinceStandard(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    province: str = pydantic.Field(
        alias="province",
    )
    """
    Two-letter CA province code ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """
