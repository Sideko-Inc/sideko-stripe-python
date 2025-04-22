import pydantic
import typing


class SourceReceiverFlow(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    """
    The address of the receiver source. This is the value that should be communicated to the customer to send their funds to.
    """
    amount_charged: int = pydantic.Field(
        alias="amount_charged",
    )
    """
    The total amount that was moved to your balance. This is almost always equal to the amount charged. In rare cases when customers deposit excess funds and we are unable to refund those, those funds get moved to your balance and show up in amount_charged as well. The amount charged is expressed in the source's currency.
    """
    amount_received: int = pydantic.Field(
        alias="amount_received",
    )
    """
    The total amount received by the receiver source. `amount_received = amount_returned + amount_charged` should be true for consumed sources unless customers deposit excess funds. The amount received is expressed in the source's currency.
    """
    amount_returned: int = pydantic.Field(
        alias="amount_returned",
    )
    """
    The total amount that was returned to the customer. The amount returned is expressed in the source's currency.
    """
    refund_attributes_method: str = pydantic.Field(
        alias="refund_attributes_method",
    )
    """
    Type of refund attribute method, one of `email`, `manual`, or `none`.
    """
    refund_attributes_status: str = pydantic.Field(
        alias="refund_attributes_status",
    )
    """
    Type of refund attribute status, one of `missing`, `requested`, or `available`.
    """
