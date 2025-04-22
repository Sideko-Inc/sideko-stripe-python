import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsEc(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsEc
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsEc(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsEc handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
