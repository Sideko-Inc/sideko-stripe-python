import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsVn(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsVn
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsVn(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsVn handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
