import pydantic
import typing
import typing_extensions


class SubscriptionUpdateBodyCancellationDetails(typing_extensions.TypedDict):
    """
    Details about why this subscription was cancelled
    """

    comment: typing_extensions.NotRequired[typing.Union[str, str]]

    feedback: typing_extensions.NotRequired[
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
    ]


class _SerializerSubscriptionUpdateBodyCancellationDetails(pydantic.BaseModel):
    """
    Serializer for SubscriptionUpdateBodyCancellationDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    comment: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="comment", default=None
    )
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
