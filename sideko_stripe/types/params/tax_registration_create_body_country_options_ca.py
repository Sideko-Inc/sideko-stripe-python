import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_ca_province_standard import (
    TaxRegistrationCreateBodyCountryOptionsCaProvinceStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsCaProvinceStandard,
)


class TaxRegistrationCreateBodyCountryOptionsCa(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsCa
    """

    province_standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsCaProvinceStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["province_standard", "simplified", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsCa(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsCa handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    province_standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsCaProvinceStandard
    ] = pydantic.Field(alias="province_standard", default=None)
    type_: typing_extensions.Literal["province_standard", "simplified", "standard"] = (
        pydantic.Field(
            alias="type",
        )
    )
