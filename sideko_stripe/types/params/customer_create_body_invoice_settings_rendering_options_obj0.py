import pydantic
import typing
import typing_extensions


class CustomerCreateBodyInvoiceSettingsRenderingOptionsObj0(
    typing_extensions.TypedDict
):
    """
    CustomerCreateBodyInvoiceSettingsRenderingOptionsObj0
    """

    amount_tax_display: typing_extensions.NotRequired[
        typing_extensions.Literal["exclude_tax", "include_inclusive_tax"]
    ]

    template: typing_extensions.NotRequired[str]


class _SerializerCustomerCreateBodyInvoiceSettingsRenderingOptionsObj0(
    pydantic.BaseModel
):
    """
    Serializer for CustomerCreateBodyInvoiceSettingsRenderingOptionsObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_tax_display: typing.Optional[
        typing_extensions.Literal["exclude_tax", "include_inclusive_tax"]
    ] = pydantic.Field(alias="amount_tax_display", default=None)
    template: typing.Optional[str] = pydantic.Field(alias="template", default=None)
