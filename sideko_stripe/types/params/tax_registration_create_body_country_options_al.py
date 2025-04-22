import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsAl(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsAl
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsAl(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsAl handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
