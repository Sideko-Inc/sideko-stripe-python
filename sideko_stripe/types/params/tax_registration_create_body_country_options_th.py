import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsTh(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsTh
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsTh(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsTh handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
