import pydantic
import typing

from .tax_product_resource_tax_settings_status_details_resource_pending import (
    TaxProductResourceTaxSettingsStatusDetailsResourcePending,
)


class TaxProductResourceTaxSettingsStatusDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="active", default=None
    )
    pending: typing.Optional[
        TaxProductResourceTaxSettingsStatusDetailsResourcePending
    ] = pydantic.Field(alias="pending", default=None)
