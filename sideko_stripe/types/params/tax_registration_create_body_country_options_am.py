import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsAm(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsAm
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsAm(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsAm handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
