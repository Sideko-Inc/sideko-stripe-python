import pydantic
import typing
import typing_extensions


class InvoiceLineUpdateBodyPricing(typing_extensions.TypedDict):
    """
    The pricing information for the invoice item.
    """

    price: typing_extensions.NotRequired[str]


class _SerializerInvoiceLineUpdateBodyPricing(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateBodyPricing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
