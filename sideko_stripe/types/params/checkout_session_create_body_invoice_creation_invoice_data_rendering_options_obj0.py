import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0
    """

    amount_tax_display: typing_extensions.NotRequired[
        typing_extensions.Literal["exclude_tax", "include_inclusive_tax"]
    ]


class _SerializerCheckoutSessionCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyInvoiceCreationInvoiceDataRenderingOptionsObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_tax_display: typing.Optional[
        typing_extensions.Literal["exclude_tax", "include_inclusive_tax"]
    ] = pydantic.Field(alias="amount_tax_display", default=None)
