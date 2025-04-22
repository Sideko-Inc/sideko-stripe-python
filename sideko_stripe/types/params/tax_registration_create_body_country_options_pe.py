import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsPe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsPe
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsPe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsPe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
