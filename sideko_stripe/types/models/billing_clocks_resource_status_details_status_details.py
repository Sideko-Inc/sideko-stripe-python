import pydantic
import typing

from .billing_clocks_resource_status_details_advancing_status_details import (
    BillingClocksResourceStatusDetailsAdvancingStatusDetails,
)


class BillingClocksResourceStatusDetailsStatusDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    advancing: typing.Optional[
        BillingClocksResourceStatusDetailsAdvancingStatusDetails
    ] = pydantic.Field(alias="advancing", default=None)
