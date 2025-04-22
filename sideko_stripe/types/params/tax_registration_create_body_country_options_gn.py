import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsGn(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsGn
    """

    type_: typing_extensions.Required[typing_extensions.Literal["standard"]]


class _SerializerTaxRegistrationCreateBodyCountryOptionsGn(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsGn handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["standard"] = pydantic.Field(
        alias="type",
    )
