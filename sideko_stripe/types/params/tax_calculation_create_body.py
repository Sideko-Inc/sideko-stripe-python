import pydantic
import typing
import typing_extensions

from .tax_calculation_create_body_customer_details import (
    TaxCalculationCreateBodyCustomerDetails,
    _SerializerTaxCalculationCreateBodyCustomerDetails,
)
from .tax_calculation_create_body_line_items_item import (
    TaxCalculationCreateBodyLineItemsItem,
    _SerializerTaxCalculationCreateBodyLineItemsItem,
)
from .tax_calculation_create_body_ship_from_details import (
    TaxCalculationCreateBodyShipFromDetails,
    _SerializerTaxCalculationCreateBodyShipFromDetails,
)
from .tax_calculation_create_body_shipping_cost import (
    TaxCalculationCreateBodyShippingCost,
    _SerializerTaxCalculationCreateBodyShippingCost,
)


class TaxCalculationCreateBody(typing_extensions.TypedDict, total=False):
    """
    TaxCalculationCreateBody
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: typing_extensions.NotRequired[str]
    """
    The ID of an existing customer to use for this calculation. If provided, the customer's address and tax IDs are copied to `customer_details`.
    """

    customer_details: typing_extensions.NotRequired[
        TaxCalculationCreateBodyCustomerDetails
    ]
    """
    Details about the customer, including address and tax IDs.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    line_items: typing_extensions.Required[
        typing.List[TaxCalculationCreateBodyLineItemsItem]
    ]
    """
    A list of items the customer is purchasing.
    """

    ship_from_details: typing_extensions.NotRequired[
        TaxCalculationCreateBodyShipFromDetails
    ]
    """
    Details about the address from which the goods are being shipped.
    """

    shipping_cost: typing_extensions.NotRequired[TaxCalculationCreateBodyShippingCost]
    """
    Shipping cost details to be used for the calculation.
    """

    tax_date: typing_extensions.NotRequired[int]
    """
    Timestamp of date at which the tax rules and rates in effect applies for the calculation. Measured in seconds since the Unix epoch. Can be up to 48 hours in the past, and up to 48 hours in the future.
    """


class _SerializerTaxCalculationCreateBody(pydantic.BaseModel):
    """
    Serializer for TaxCalculationCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    currency: str = pydantic.Field(
        alias="currency",
    )
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    customer_details: typing.Optional[
        _SerializerTaxCalculationCreateBodyCustomerDetails
    ] = pydantic.Field(alias="customer_details", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    line_items: typing.List[_SerializerTaxCalculationCreateBodyLineItemsItem] = (
        pydantic.Field(
            alias="line_items",
        )
    )
    ship_from_details: typing.Optional[
        _SerializerTaxCalculationCreateBodyShipFromDetails
    ] = pydantic.Field(alias="ship_from_details", default=None)
    shipping_cost: typing.Optional[_SerializerTaxCalculationCreateBodyShippingCost] = (
        pydantic.Field(alias="shipping_cost", default=None)
    )
    tax_date: typing.Optional[int] = pydantic.Field(alias="tax_date", default=None)
