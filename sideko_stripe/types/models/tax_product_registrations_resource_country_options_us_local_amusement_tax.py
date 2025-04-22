import pydantic


class TaxProductRegistrationsResourceCountryOptionsUsLocalAmusementTax(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    jurisdiction: str = pydantic.Field(
        alias="jurisdiction",
    )
    """
    A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction.
    """
