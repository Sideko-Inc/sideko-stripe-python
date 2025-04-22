import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_mt_standard import (
    TaxRegistrationCreateBodyCountryOptionsMtStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsMtStandard,
)


class TaxRegistrationCreateBodyCountryOptionsMt(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsMt
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsMtStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsMt(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsMt handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsMtStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
