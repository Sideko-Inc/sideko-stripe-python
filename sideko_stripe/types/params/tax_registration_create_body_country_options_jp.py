import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsJp(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsJp
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsJp(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsJp handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
