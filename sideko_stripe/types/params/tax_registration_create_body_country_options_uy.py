import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsUy(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsUy
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsUy(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsUy handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
