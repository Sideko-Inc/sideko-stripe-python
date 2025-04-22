import pydantic
import typing
import typing_extensions


class InvoiceCreateBodyTransferData(typing_extensions.TypedDict):
    """
    If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice's charge.
    """

    amount: typing_extensions.NotRequired[int]

    destination: typing_extensions.Required[str]


class _SerializerInvoiceCreateBodyTransferData(pydantic.BaseModel):
    """
    Serializer for InvoiceCreateBodyTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    destination: str = pydantic.Field(
        alias="destination",
    )
