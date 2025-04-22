import pydantic
import typing
import typing_extensions


class RefundDestinationDetailsCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    Value of the reference number assigned to the refund.
    """
    reference_status: typing.Optional[str] = pydantic.Field(
        alias="reference_status", default=None
    )
    """
    Status of the reference number on the refund. This can be `pending`, `available` or `unavailable`.
    """
    reference_type: typing.Optional[str] = pydantic.Field(
        alias="reference_type", default=None
    )
    """
    Type of the reference number assigned to the refund.
    """
    type_: typing_extensions.Literal["pending", "refund", "reversal"] = pydantic.Field(
        alias="type",
    )
    """
    The type of refund. This can be `refund`, `reversal`, or `pending`.
    """
