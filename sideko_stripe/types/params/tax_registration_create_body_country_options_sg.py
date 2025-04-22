import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsSg(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsSg
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsSg(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsSg handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
