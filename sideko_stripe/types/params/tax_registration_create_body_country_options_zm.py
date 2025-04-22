import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsZm(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsZm
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsZm(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsZm handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
