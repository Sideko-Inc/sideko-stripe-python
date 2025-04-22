import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsRs(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsRs
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsRs(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsRs handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
