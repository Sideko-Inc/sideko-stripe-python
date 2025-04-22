import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsMx(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsMx
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsMx(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsMx handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
