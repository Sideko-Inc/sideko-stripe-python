import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsSn(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsSn
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsSn(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsSn handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
