import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_de_standard import (
    TaxRegistrationCreateBodyCountryOptionsDeStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsDeStandard,
)


class TaxRegistrationCreateBodyCountryOptionsDe(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsDe
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsDeStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsDe(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsDe handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsDeStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
