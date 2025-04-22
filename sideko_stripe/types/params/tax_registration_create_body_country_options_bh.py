import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsBh(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsBh
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsBh(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsBh handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
