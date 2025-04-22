import pydantic
import typing_extensions


class TaxProductRegistrationsResourceCountryOptionsEuStandard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    place_of_supply_scheme: typing_extensions.Literal["small_seller", "standard"] = (
        pydantic.Field(
            alias="place_of_supply_scheme",
        )
    )
    """
    Place of supply scheme used in an EU standard registration.
    """
