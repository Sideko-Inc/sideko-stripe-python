import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsBa(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsBa
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsBa(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsBa handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
