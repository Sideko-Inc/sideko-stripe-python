import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsRu(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsRu
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsRu(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsRu handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
