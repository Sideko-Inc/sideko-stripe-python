import pydantic
import typing


class RefundDestinationDetailsBlik(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    network_decline_code: typing.Optional[str] = pydantic.Field(
        alias="network_decline_code", default=None
    )
    """
    For refunds declined by the network, a decline code provided by the network which indicates the reason the refund failed.
    """
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
