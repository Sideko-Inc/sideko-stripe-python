import pydantic
import typing
import typing_extensions


class CreditNotePreview1RefundsItem(typing_extensions.TypedDict):
    """
    CreditNotePreview1RefundsItem
    """

    amount_refunded: typing_extensions.NotRequired[int]

    refund: typing_extensions.NotRequired[str]


class _SerializerCreditNotePreview1RefundsItem(pydantic.BaseModel):
    """
    Serializer for CreditNotePreview1RefundsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_refunded: typing.Optional[int] = pydantic.Field(
        alias="amount_refunded", default=None
    )
    refund: typing.Optional[str] = pydantic.Field(alias="refund", default=None)
