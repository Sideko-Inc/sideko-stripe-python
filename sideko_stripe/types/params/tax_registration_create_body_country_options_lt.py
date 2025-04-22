import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_lt_standard import (
    TaxRegistrationCreateBodyCountryOptionsLtStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsLtStandard,
)


class TaxRegistrationCreateBodyCountryOptionsLt(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsLt
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsLtStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsLt(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsLt handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsLtStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
