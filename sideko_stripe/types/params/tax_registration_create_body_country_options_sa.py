import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsSa(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsSa
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsSa(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsSa handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
