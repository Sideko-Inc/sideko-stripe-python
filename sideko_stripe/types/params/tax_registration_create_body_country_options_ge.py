import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsGe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsGe
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsGe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsGe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
