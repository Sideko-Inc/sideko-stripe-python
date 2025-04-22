import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsUz(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsUz
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsUz(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsUz handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
