import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsMe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsMe
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsMe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsMe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
