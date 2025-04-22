import pydantic
import typing


class TreasuryOutboundPaymentsResourceOutboundPaymentResourceStatusTransitions(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    canceled_at: typing.Optional[int] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    Timestamp describing when an OutboundPayment changed status to `canceled`.
    """
    failed_at: typing.Optional[int] = pydantic.Field(alias="failed_at", default=None)
    """
    Timestamp describing when an OutboundPayment changed status to `failed`.
    """
    posted_at: typing.Optional[int] = pydantic.Field(alias="posted_at", default=None)
    """
    Timestamp describing when an OutboundPayment changed status to `posted`.
    """
    returned_at: typing.Optional[int] = pydantic.Field(
        alias="returned_at", default=None
    )
    """
    Timestamp describing when an OutboundPayment changed status to `returned`.
    """
