import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_pl_standard import (
    TaxRegistrationCreateBodyCountryOptionsPlStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsPlStandard,
)


class TaxRegistrationCreateBodyCountryOptionsPl(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsPl
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsPlStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsPl(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsPl handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsPlStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
