import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_hu_standard import (
    TaxRegistrationCreateBodyCountryOptionsHuStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsHuStandard,
)


class TaxRegistrationCreateBodyCountryOptionsHu(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsHu
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsHuStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsHu(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsHu handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsHuStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
