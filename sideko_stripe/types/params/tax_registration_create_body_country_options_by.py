import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsBy(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsBy
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsBy(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsBy handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
