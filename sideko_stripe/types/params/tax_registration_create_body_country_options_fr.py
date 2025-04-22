import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_fr_standard import (
    TaxRegistrationCreateBodyCountryOptionsFrStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsFrStandard,
)


class TaxRegistrationCreateBodyCountryOptionsFr(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsFr
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsFrStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsFr(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsFr handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsFrStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
