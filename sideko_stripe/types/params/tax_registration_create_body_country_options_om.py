import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsOm(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsOm
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsOm(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsOm handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
