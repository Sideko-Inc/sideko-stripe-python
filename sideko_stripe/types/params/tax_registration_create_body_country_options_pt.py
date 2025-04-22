import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_pt_standard import (
    TaxRegistrationCreateBodyCountryOptionsPtStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsPtStandard,
)


class TaxRegistrationCreateBodyCountryOptionsPt(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsPt
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsPtStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsPt(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsPt handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsPtStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
