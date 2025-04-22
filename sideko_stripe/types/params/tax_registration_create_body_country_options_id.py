import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsId(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsId
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsId(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsId handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
