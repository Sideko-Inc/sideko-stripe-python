import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsCr(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsCr
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsCr(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsCr handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
