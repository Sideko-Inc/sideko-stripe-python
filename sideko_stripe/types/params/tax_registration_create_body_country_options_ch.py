import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsCh(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsCh
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsCh(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsCh handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
