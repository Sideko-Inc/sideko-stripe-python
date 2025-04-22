import pydantic
import typing
import typing_extensions


class CreditNotePreviewRefundsItem(typing_extensions.TypedDict):
    """
    CreditNotePreviewRefundsItem
    """

    amount_refunded: typing_extensions.NotRequired[int]

    refund: typing_extensions.NotRequired[str]


class _SerializerCreditNotePreviewRefundsItem(pydantic.BaseModel):
    """
    Serializer for CreditNotePreviewRefundsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_refunded: typing.Optional[int] = pydantic.Field(
        alias="amount_refunded", default=None
    )
    refund: typing.Optional[str] = pydantic.Field(alias="refund", default=None)
