import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsBb(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsBb
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsBb(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsBb handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
