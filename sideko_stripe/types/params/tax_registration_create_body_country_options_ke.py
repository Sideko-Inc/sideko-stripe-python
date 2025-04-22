import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsKe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsKe
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsKe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsKe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
