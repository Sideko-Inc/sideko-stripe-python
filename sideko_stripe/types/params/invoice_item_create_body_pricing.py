import pydantic
import typing
import typing_extensions


class InvoiceItemCreateBodyPricing(typing_extensions.TypedDict):
    """
    The pricing information for the invoice item.
    """

    price: typing_extensions.NotRequired[str]


class _SerializerInvoiceItemCreateBodyPricing(pydantic.BaseModel):
    """
    Serializer for InvoiceItemCreateBodyPricing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
