import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsKh(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsKh
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsKh(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsKh handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
