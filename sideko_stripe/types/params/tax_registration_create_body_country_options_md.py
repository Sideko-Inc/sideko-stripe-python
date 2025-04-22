import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsMd(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsMd
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsMd(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsMd handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
