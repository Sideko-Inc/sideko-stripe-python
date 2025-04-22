import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsGb(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsGb
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsGb(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsGb handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
