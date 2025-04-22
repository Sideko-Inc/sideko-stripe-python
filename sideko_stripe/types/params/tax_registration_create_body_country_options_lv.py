import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_lv_standard import (
    TaxRegistrationCreateBodyCountryOptionsLvStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsLvStandard,
)


class TaxRegistrationCreateBodyCountryOptionsLv(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsLv
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsLvStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsLv(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsLv handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsLvStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
