import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_ro_standard import (
    TaxRegistrationCreateBodyCountryOptionsRoStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsRoStandard,
)


class TaxRegistrationCreateBodyCountryOptionsRo(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsRo
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsRoStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsRo(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsRo handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsRoStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
