import pydantic
import typing
import typing_extensions


class InvoiceUpdateBodyTransferDataObj0(typing_extensions.TypedDict):
    """
    InvoiceUpdateBodyTransferDataObj0
    """

    amount: typing_extensions.NotRequired[int]

    destination: typing_extensions.Required[str]


class _SerializerInvoiceUpdateBodyTransferDataObj0(pydantic.BaseModel):
    """
    Serializer for InvoiceUpdateBodyTransferDataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    destination: str = pydantic.Field(
        alias="destination",
    )
