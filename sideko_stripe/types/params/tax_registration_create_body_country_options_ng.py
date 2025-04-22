import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsNg(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsNg
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsNg(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsNg handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
