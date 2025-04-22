import pydantic
import typing
import typing_extensions


class CustomerUpdateBodyInvoiceSettingsRenderingOptionsObj0(
    typing_extensions.TypedDict
):
    """
    CustomerUpdateBodyInvoiceSettingsRenderingOptionsObj0
    """

    amount_tax_display: typing_extensions.NotRequired[
        typing_extensions.Literal["exclude_tax", "include_inclusive_tax"]
    ]

    template: typing_extensions.NotRequired[str]


class _SerializerCustomerUpdateBodyInvoiceSettingsRenderingOptionsObj0(
    pydantic.BaseModel
):
    """
    Serializer for CustomerUpdateBodyInvoiceSettingsRenderingOptionsObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_tax_display: typing.Optional[
        typing_extensions.Literal["exclude_tax", "include_inclusive_tax"]
    ] = pydantic.Field(alias="amount_tax_display", default=None)
    template: typing.Optional[str] = pydantic.Field(alias="template", default=None)
