import pydantic
import typing


class InvoiceSettingCustomerRenderingOptions(pydantic.BaseModel):
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
    template: typing.Optional[str] = pydantic.Field(alias="template", default=None)
    """
    ID of the invoice rendering template to be used for this customer's invoices. If set, the template will be used on all invoices for this customer unless a template is set directly on the invoice.
    """
