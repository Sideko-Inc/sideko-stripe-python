import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsNo(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsNo
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsNo(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsNo handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
