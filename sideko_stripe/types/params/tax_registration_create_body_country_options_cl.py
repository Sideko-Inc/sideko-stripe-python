import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsCl(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsCl
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsCl(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsCl handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
