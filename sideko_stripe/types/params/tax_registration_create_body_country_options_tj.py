import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsTj(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsTj
    """

    type_: typing_extensions.Required[typing_extensions.Literal["simplified"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsTj(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsTj handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["simplified"] = pydantic.Field(
        alias="type",
    )
