import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .refund import Refund


class CreditNoteRefund(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_refunded: int = pydantic.Field(
        alias="amount_refunded",
    )
    """
    Amount of the refund that applies to this credit note, in cents (or local equivalent).
    """
    refund: typing.Union[str, "Refund"] = pydantic.Field(
        alias="refund",
    )
    """
    ID of the refund.
    """
