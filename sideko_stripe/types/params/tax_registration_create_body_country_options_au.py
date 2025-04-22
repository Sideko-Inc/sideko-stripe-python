import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsAu(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsAu
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsAu(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsAu handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
