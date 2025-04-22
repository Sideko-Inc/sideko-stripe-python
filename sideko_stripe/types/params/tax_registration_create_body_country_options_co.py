import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsCo(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsCo
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsCo(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsCo handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
