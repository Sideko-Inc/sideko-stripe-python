import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_hr_standard import (
    TaxRegistrationCreateBodyCountryOptionsHrStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsHrStandard,
)


class TaxRegistrationCreateBodyCountryOptionsHr(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsHr
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsHrStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsHr(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsHr handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsHrStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
