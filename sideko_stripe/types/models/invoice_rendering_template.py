import pydantic
import typing
import typing_extensions

from .invoice_rendering_template_metadata import InvoiceRenderingTemplateMetadata


class InvoiceRenderingTemplate(pydantic.BaseModel):
    """
    Invoice Rendering Templates are used to configure how invoices are rendered on surfaces like the PDF. Invoice Rendering Templates
    can be created from within the Dashboard, and they can be used over the API when creating invoices.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[InvoiceRenderingTemplateMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nickname: typing.Optional[str] = pydantic.Field(alias="nickname", default=None)
    """
    A brief description of the template, hidden from customers
    """
    object: typing_extensions.Literal["invoice_rendering_template"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["active", "archived"] = pydantic.Field(
        alias="status",
    )
    """
    The status of the template, one of `active` or `archived`.
    """
    version: int = pydantic.Field(
        alias="version",
    )
    """
    Version of this template; version increases by one when an update on the template changes any field that controls invoice rendering
    """
