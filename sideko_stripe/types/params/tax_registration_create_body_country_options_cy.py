import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_cy_standard import (
    TaxRegistrationCreateBodyCountryOptionsCyStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsCyStandard,
)


class TaxRegistrationCreateBodyCountryOptionsCy(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsCy
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsCyStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsCy(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsCy handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsCyStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
