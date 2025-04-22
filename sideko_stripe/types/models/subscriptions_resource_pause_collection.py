import pydantic
import typing
import typing_extensions


class SubscriptionsResourcePauseCollection(pydantic.BaseModel):
    """
    The Pause Collection settings determine how we will pause collection for this subscription and for how long the subscription
    should be paused.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    behavior: typing_extensions.Literal[
        "keep_as_draft", "mark_uncollectible", "void"
    ] = pydantic.Field(
        alias="behavior",
    )
    """
    The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
    """
    resumes_at: typing.Optional[int] = pydantic.Field(alias="resumes_at", default=None)
    """
    The time after which the subscription will resume collecting payments.
    """
