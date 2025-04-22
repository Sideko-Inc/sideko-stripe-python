import pydantic

from .address import Address


class TaxProductResourceTaxSettingsHeadOffice(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: Address = pydantic.Field(
        alias="address",
    )
