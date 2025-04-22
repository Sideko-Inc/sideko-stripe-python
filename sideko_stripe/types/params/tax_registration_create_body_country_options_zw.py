import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsZw(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsZw
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsZw(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsZw handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
