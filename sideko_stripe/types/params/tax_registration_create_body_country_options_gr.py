import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_gr_standard import (
    TaxRegistrationCreateBodyCountryOptionsGrStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsGrStandard,
)


class TaxRegistrationCreateBodyCountryOptionsGr(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsGr
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsGrStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsGr(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsGr handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsGrStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
