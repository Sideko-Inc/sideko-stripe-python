import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_ee_standard import (
    TaxRegistrationCreateBodyCountryOptionsEeStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsEeStandard,
)


class TaxRegistrationCreateBodyCountryOptionsEe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsEe
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsEeStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsEe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsEe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsEeStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
