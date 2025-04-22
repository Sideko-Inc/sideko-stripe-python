import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsMy(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsMy
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsMy(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsMy handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
