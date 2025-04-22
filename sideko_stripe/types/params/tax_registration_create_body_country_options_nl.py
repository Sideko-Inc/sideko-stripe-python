import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_nl_standard import (
    TaxRegistrationCreateBodyCountryOptionsNlStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsNlStandard,
)


class TaxRegistrationCreateBodyCountryOptionsNl(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsNl
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsNlStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsNl(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsNl handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsNlStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
