import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_es_standard import (
    TaxRegistrationCreateBodyCountryOptionsEsStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsEsStandard,
)


class TaxRegistrationCreateBodyCountryOptionsEs(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsEs
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsEsStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsEs(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsEs handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsEsStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
