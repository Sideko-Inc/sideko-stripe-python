import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_be_standard import (
    TaxRegistrationCreateBodyCountryOptionsBeStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsBeStandard,
)


class TaxRegistrationCreateBodyCountryOptionsBe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsBe
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsBeStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsBe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsBe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsBeStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
