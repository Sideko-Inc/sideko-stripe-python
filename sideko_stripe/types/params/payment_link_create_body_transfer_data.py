import pydantic
import typing
import typing_extensions


class PaymentLinkCreateBodyTransferData(typing_extensions.TypedDict):
    """
    The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.
    """

    amount: typing_extensions.NotRequired[int]

    destination: typing_extensions.Required[str]


class _SerializerPaymentLinkCreateBodyTransferData(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    destination: str = pydantic.Field(
        alias="destination",
    )
