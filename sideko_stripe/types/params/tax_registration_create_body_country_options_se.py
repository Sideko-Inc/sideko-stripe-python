import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_se_standard import (
    TaxRegistrationCreateBodyCountryOptionsSeStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsSeStandard,
)


class TaxRegistrationCreateBodyCountryOptionsSe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsSe
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsSeStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsSe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsSe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsSeStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
