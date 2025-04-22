import pydantic
import typing
import typing_extensions


class CancellationDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    comment: typing.Optional[str] = pydantic.Field(alias="comment", default=None)
    """
    Additional comments about why the user canceled the subscription, if the subscription was canceled explicitly by the user.
    """
    feedback: typing.Optional[
        typing_extensions.Literal[
            "customer_service",
            "low_quality",
            "missing_features",
            "other",
            "switched_service",
            "too_complex",
            "too_expensive",
            "unused",
        ]
    ] = pydantic.Field(alias="feedback", default=None)
    """
    The customer submitted reason for why they canceled, if the subscription was canceled explicitly by the user.
    """
    reason: typing.Optional[
        typing_extensions.Literal[
            "cancellation_requested", "payment_disputed", "payment_failed"
        ]
    ] = pydantic.Field(alias="reason", default=None)
    """
    Why this subscription was canceled.
    """
