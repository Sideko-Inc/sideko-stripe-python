import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsSr(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsSr
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsSr(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsSr handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
