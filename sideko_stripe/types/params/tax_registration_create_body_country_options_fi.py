import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_fi_standard import (
    TaxRegistrationCreateBodyCountryOptionsFiStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsFiStandard,
)


class TaxRegistrationCreateBodyCountryOptionsFi(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsFi
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsFiStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsFi(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsFi handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsFiStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
