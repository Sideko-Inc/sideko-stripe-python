import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_lu_standard import (
    TaxRegistrationCreateBodyCountryOptionsLuStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsLuStandard,
)


class TaxRegistrationCreateBodyCountryOptionsLu(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsLu
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsLuStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsLu(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsLu handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsLuStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
