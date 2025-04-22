import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsMa(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsMa
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsMa(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsMa handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
