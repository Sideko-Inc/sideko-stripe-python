import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsZa(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsZa
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsZa(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsZa handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
