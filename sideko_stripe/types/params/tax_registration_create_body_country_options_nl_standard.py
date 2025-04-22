import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsNlStandard(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsNlStandard
    """

    place_of_supply_scheme: typing_extensions.Required[
        typing_extensions.Literal["small_seller", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsNlStandard(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsNlStandard handling case conversions
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
