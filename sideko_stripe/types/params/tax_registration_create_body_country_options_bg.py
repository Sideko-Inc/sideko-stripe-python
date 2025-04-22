import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_bg_standard import (
    TaxRegistrationCreateBodyCountryOptionsBgStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsBgStandard,
)


class TaxRegistrationCreateBodyCountryOptionsBg(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsBg
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsBgStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsBg(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsBg handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsBgStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
