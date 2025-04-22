import pydantic
import typing
import typing_extensions

from .tax_product_resource_customer_details_resource_tax_id import (
    TaxProductResourceCustomerDetailsResourceTaxId,
)
from .tax_product_resource_postal_address import TaxProductResourcePostalAddress


class TaxProductResourceCustomerDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[TaxProductResourcePostalAddress] = pydantic.Field(
        alias="address", default=None
    )
    address_source: typing.Optional[
        typing_extensions.Literal["billing", "shipping"]
    ] = pydantic.Field(alias="address_source", default=None)
    """
    The type of customer address provided.
    """
    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    """
    The customer's IP address (IPv4 or IPv6).
    """
    tax_ids: typing.List[TaxProductResourceCustomerDetailsResourceTaxId] = (
        pydantic.Field(
            alias="tax_ids",
        )
    )
    """
    The customer's tax IDs (for example, EU VAT numbers).
    """
    taxability_override: typing_extensions.Literal[
        "customer_exempt", "none", "reverse_charge"
    ] = pydantic.Field(
        alias="taxability_override",
    )
    """
    The taxability override used for taxation.
    """
