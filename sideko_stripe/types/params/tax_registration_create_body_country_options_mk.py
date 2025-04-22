import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsMk(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsMk
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsMk(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsMk handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
