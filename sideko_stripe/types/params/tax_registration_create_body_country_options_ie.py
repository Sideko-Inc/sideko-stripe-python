import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_ie_standard import (
    TaxRegistrationCreateBodyCountryOptionsIeStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsIeStandard,
)


class TaxRegistrationCreateBodyCountryOptionsIe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsIe
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsIeStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsIe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsIe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsIeStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
