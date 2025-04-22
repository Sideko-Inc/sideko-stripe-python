import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsFiStandard(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsFiStandard
    """

    place_of_supply_scheme: typing_extensions.Required[
        typing_extensions.Literal["small_seller", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsFiStandard(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsFiStandard handling case conversions
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
