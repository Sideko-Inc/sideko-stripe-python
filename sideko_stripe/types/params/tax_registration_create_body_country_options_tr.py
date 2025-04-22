import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsTr(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsTr
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsTr(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsTr handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
