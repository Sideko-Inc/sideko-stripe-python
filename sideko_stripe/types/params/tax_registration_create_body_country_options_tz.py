import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsTz(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsTz
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsTz(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsTz handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
