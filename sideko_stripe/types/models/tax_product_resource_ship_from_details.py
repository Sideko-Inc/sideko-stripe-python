import pydantic

from .tax_product_resource_postal_address import TaxProductResourcePostalAddress


class TaxProductResourceShipFromDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: TaxProductResourcePostalAddress = pydantic.Field(
        alias="address",
    )
