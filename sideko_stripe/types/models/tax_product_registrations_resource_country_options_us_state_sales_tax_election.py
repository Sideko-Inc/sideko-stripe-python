import pydantic
import typing
import typing_extensions


class TaxProductRegistrationsResourceCountryOptionsUsStateSalesTaxElection(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    jurisdiction: typing.Optional[str] = pydantic.Field(
        alias="jurisdiction", default=None
    )
    """
    A [FIPS code](https://www.census.gov/library/reference/code-lists/ansi.html) representing the local jurisdiction.
    """
    type_: typing_extensions.Literal[
        "local_use_tax", "simplified_sellers_use_tax", "single_local_use_tax"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of the election for the state sales tax registration.
    """
