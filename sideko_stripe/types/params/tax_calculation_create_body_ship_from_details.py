import pydantic
import typing_extensions

from .tax_calculation_create_body_ship_from_details_address import (
    TaxCalculationCreateBodyShipFromDetailsAddress,
    _SerializerTaxCalculationCreateBodyShipFromDetailsAddress,
)


class TaxCalculationCreateBodyShipFromDetails(typing_extensions.TypedDict):
    """
    Details about the address from which the goods are being shipped.
    """

    address: typing_extensions.Required[TaxCalculationCreateBodyShipFromDetailsAddress]


class _SerializerTaxCalculationCreateBodyShipFromDetails(pydantic.BaseModel):
    """
    Serializer for TaxCalculationCreateBodyShipFromDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerTaxCalculationCreateBodyShipFromDetailsAddress = pydantic.Field(
        alias="address",
    )
