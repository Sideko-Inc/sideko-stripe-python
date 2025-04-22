import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_sk_standard import (
    TaxRegistrationCreateBodyCountryOptionsSkStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsSkStandard,
)


class TaxRegistrationCreateBodyCountryOptionsSk(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsSk
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsSkStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsSk(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsSk handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsSkStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
