import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_cz_standard import (
    TaxRegistrationCreateBodyCountryOptionsCzStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsCzStandard,
)


class TaxRegistrationCreateBodyCountryOptionsCz(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsCz
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsCzStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsCz(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsCz handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsCzStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
