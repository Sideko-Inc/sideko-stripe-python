import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsCd(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsCd
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsCd(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsCd handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
