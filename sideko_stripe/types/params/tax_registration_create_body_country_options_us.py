import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_us_local_amusement_tax import (
    TaxRegistrationCreateBodyCountryOptionsUsLocalAmusementTax,
    _SerializerTaxRegistrationCreateBodyCountryOptionsUsLocalAmusementTax,
)
from .tax_registration_create_body_country_options_us_local_lease_tax import (
    TaxRegistrationCreateBodyCountryOptionsUsLocalLeaseTax,
    _SerializerTaxRegistrationCreateBodyCountryOptionsUsLocalLeaseTax,
)
from .tax_registration_create_body_country_options_us_state_sales_tax import (
    TaxRegistrationCreateBodyCountryOptionsUsStateSalesTax,
    _SerializerTaxRegistrationCreateBodyCountryOptionsUsStateSalesTax,
)


class TaxRegistrationCreateBodyCountryOptionsUs(typing_extensions.TypedDict):
    """
    TaxRegistrationCreateBodyCountryOptionsUs
    """

    local_amusement_tax: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsUsLocalAmusementTax
    ]

    local_lease_tax: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsUsLocalLeaseTax
    ]

    state: typing_extensions.Required[str]

    state_sales_tax: typing_extensions.NotRequired[
        TaxRegistrationCreateBodyCountryOptionsUsStateSalesTax
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal[
            "local_amusement_tax",
            "local_lease_tax",
            "state_communications_tax",
            "state_retail_delivery_fee",
            "state_sales_tax",
        ]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsUs(pydantic.BaseModel):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsUs handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    local_amusement_tax: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsUsLocalAmusementTax
    ] = pydantic.Field(alias="local_amusement_tax", default=None)
    local_lease_tax: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsUsLocalLeaseTax
    ] = pydantic.Field(alias="local_lease_tax", default=None)
    state: str = pydantic.Field(
        alias="state",
    )
    state_sales_tax: typing.Optional[
        _SerializerTaxRegistrationCreateBodyCountryOptionsUsStateSalesTax
    ] = pydantic.Field(alias="state_sales_tax", default=None)
    type_: typing_extensions.Literal[
        "local_amusement_tax",
        "local_lease_tax",
        "state_communications_tax",
        "state_retail_delivery_fee",
        "state_sales_tax",
    ] = pydantic.Field(
        alias="type",
    )
