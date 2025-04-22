import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsKz(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsKz
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsKz(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsKz handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
