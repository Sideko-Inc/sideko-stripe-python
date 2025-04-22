import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsNz(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsNz
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsNz(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsNz handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
