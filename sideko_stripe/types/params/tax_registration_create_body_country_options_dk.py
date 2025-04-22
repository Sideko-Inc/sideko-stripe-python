import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_dk_standard import (
    TaxRegistrationCreateBodyCountryOptionsDkStandard,
    _SerializerTaxRegistrationCreateBodyCountryOptionsDkStandard,
)


class TaxRegistrationCreateBodyCountryOptionsDk(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsDk
    """

    standard: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsDkStandard
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ioss", "oss_non_union", "oss_union", "standard"]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsDk(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsDk handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    standard: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsDkStandard
    ] = pydantic.Field(alias="standard", default=None)
    type_: typing_extensions.Literal[
        "ioss", "oss_non_union", "oss_union", "standard"
    ] = pydantic.Field(
        alias="type",
    )
