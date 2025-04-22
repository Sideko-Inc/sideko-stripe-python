import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_si_standard import (
    TaxRegistrationCreateBodyCountryOptionsSiStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsSiStandard,
)


class TaxRegistrationCreateBodyCountryOptionsSi(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsSi
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsSiStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsSi(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsSi handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsSiStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
