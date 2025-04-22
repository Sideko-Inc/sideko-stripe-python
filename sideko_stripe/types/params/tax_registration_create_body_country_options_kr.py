import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsKr(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsKr
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsKr(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsKr handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
