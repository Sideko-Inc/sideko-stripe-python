import pydantic
import typing


class RefundDestinationDetailsEuBankTransfer(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    The reference assigned to the refund.
    """
    reference_status: typing.Optional[str] = pydantic.Field(
        alias="reference_status", default=None
    )
    """
    Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
    """
