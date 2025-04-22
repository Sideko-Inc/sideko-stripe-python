import pydantic
import typing
import typing_extensions

from .tax_registration_create_body_country_options_us_state_sales_tax_elections_item import (
    TaxRegistrationCreateBodyCountryOptionsUsStateSalesTaxElectionsItem,
    _SerializerTaxRegistrationCreateBodyCountryOptionsUsStateSalesTaxElectionsItem,
)


class TaxRegistrationCreateBodyCountryOptionsUsStateSalesTax(
    typing_extensions.TypedDict
):
    """
    TaxRegistrationCreateBodyCountryOptionsUsStateSalesTax
    """

    elections: typing_extensions.Required[
        typing.List[TaxRegistrationCreateBodyCountryOptionsUsStateSalesTaxElectionsItem]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsUsStateSalesTax(
    pydantic.BaseModel
):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsUsStateSalesTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    elections: typing.List[
        _SerializerTaxRegistrationCreateBodyCountryOptionsUsStateSalesTaxElectionsItem
    ] = pydantic.Field(
        alias="elections",
    )
