import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_at_standard import (
    TaxRegistrationCreateBodyCountryOptionsAtStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsAtStandard,
)


class TaxRegistrationCreateBodyCountryOptionsAt(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsAt
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsAtStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsAt(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsAt handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsAtStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
