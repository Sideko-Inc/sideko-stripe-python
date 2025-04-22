import pydantic
import typing


class InvoiceInstallmentsCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    """
    Whether Installments are enabled for this Invoice.
    """
