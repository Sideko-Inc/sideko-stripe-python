import pydantic
import typing
import typing_extensions


class CustomerSubscriptionModifyBodyPauseCollectionObj0(typing_extensions.TypedDict):
    """
    CustomerSubscriptionModifyBodyPauseCollectionObj0
    """

    behavior: typing_extensions.Required[
        typing_extensions.Literal["keep_as_draft", "mark_uncollectible", "void"]
    ]

    resumes_at: typing_extensions.NotRequired[int]


class _SerializerCustomerSubscriptionModifyBodyPauseCollectionObj0(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionModifyBodyPauseCollectionObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    behavior: typing_extensions.Literal[
        "keep_as_draft", "mark_uncollectible", "void"
    ] = pydantic.Field(
        alias="behavior",
    )
    resumes_at: typing.Optional[int] = pydantic.Field(alias="resumes_at", default=None)
