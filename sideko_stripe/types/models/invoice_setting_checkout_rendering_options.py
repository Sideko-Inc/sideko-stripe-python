import pydantic
import typing


class InvoiceSettingCheckoutRenderingOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_tax_display: typing.Optional[str] = pydantic.Field(
        alias="amount_tax_display", default=None
    )
    """
    How line-item prices and amounts will be displayed with respect to tax on invoice PDFs.
    """
