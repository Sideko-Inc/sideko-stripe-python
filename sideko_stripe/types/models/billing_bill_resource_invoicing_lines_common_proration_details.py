import pydantic
import typing

from .billing_bill_resource_invoicing_lines_common_credited_items import (
    BillingBillResourceInvoicingLinesCommonCreditedItems,
)


class BillingBillResourceInvoicingLinesCommonProrationDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credited_items: typing.Optional[
        BillingBillResourceInvoicingLinesCommonCreditedItems
    ] = pydantic.Field(alias="credited_items", default=None)
