import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsAo(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsAo
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsAo(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsAo handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
