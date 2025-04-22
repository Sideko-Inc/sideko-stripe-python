import pydantic
import typing


class InvoicesResourceStatusTransitions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    finalized_at: typing.Optional[int] = pydantic.Field(
        alias="finalized_at", default=None
    )
    """
    The time that the invoice draft was finalized.
    """
    marked_uncollectible_at: typing.Optional[int] = pydantic.Field(
        alias="marked_uncollectible_at", default=None
    )
    """
    The time that the invoice was marked uncollectible.
    """
    paid_at: typing.Optional[int] = pydantic.Field(alias="paid_at", default=None)
    """
    The time that the invoice was paid.
    """
    voided_at: typing.Optional[int] = pydantic.Field(alias="voided_at", default=None)
    """
    The time that the invoice was voided.
    """
