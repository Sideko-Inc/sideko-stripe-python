import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsNp(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsNp
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsNp(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsNp handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
