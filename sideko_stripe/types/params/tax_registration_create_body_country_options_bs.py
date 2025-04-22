import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsBs(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsBs
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsBs(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsBs handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
