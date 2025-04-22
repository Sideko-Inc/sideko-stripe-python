import pydantic
import typing
import typing_extensions


class TaxProductResourceJurisdiction(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: str = pydantic.Field(
        alias="country",
    )
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    """
    A human-readable name for the jurisdiction imposing the tax.
    """
    level: typing_extensions.Literal[
        "city", "country", "county", "district", "state"
    ] = pydantic.Field(
        alias="level",
    )
    """
    Indicates the level of the jurisdiction imposing the tax.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, "NY" for New York, United States.
    """
