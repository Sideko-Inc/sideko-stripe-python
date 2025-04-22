import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsIs(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsIs
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsIs(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsIs handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
