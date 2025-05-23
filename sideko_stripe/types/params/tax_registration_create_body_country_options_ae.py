import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsAe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsAe
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsAe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsAe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
