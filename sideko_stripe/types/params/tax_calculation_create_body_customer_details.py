import pydantic
import typing
import typing_extensions

from .tax_calculation_create_body_customer_details_address import (
    TaxCalculationCreateBodyCustomerDetailsAddress,
    _SerializerTaxCalculationCreateBodyCustomerDetailsAddress,
)
from .tax_calculation_create_body_customer_details_tax_ids_item import (
    TaxCalculationCreateBodyCustomerDetailsTaxIdsItem,
    _SerializerTaxCalculationCreateBodyCustomerDetailsTaxIdsItem,
)


class TaxCalculationCreateBodyCustomerDetails(typing_extensions.TypedDict):
    """
    Details about the customer, including address and tax IDs.
    """

    address: typing_extensions.NotRequired[
        TaxCalculationCreateBodyCustomerDetailsAddress
    ]

    address_source: typing_extensions.NotRequired[
        typing_extensions.Literal["billing", "shipping"]
    ]

    ip_address: typing_extensions.NotRequired[str]

    tax_ids: typing_extensions.NotRequired[
        typing.List[TaxCalculationCreateBodyCustomerDetailsTaxIdsItem]
    ]

    taxability_override: typing_extensions.NotRequired[
        typing_extensions.Literal["customer_exempt", "none", "reverse_charge"]
    ]


class _SerializerTaxCalculationCreateBodyCustomerDetails(pydantic.BaseModel):
    """
    Serializer for TaxCalculationCreateBodyCustomerDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        _SerializerTaxCalculationCreateBodyCustomerDetailsAddress
    ] = pydantic.Field(alias="address", default=None)
    address_source: typing.Optional[
        typing_extensions.Literal["billing", "shipping"]
    ] = pydantic.Field(alias="address_source", default=None)
    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    tax_ids: typing.Optional[
        typing.List[_SerializerTaxCalculationCreateBodyCustomerDetailsTaxIdsItem]
    ] = pydantic.Field(alias="tax_ids", default=None)
    taxability_override: typing.Optional[
        typing_extensions.Literal["customer_exempt", "none", "reverse_charge"]
    ] = pydantic.Field(alias="taxability_override", default=None)
