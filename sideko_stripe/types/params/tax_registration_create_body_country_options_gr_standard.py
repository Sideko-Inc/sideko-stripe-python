import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsGrStandard(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsGrStandard
    """

    place_of_supply_scheme: typing_extensions.Required[
        typing_extensions.Literal["small_seller", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsGrStandard(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsGrStandard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    place_of_supply_scheme: typing_extensions.Literal["small_seller", "standard"] = (
        pydantic.Field(
            alias="place_of_supply_scheme",
        )
    )
