import pydantic
import typing
import typing_extensions


class SubscriptionScheduleReleaseBody(typing_extensions.TypedDict, total=False):
    """
    SubscriptionScheduleReleaseBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    preserve_cancel_date: typing_extensions.NotRequired[bool]
    """
    Keep any cancellation on the subscription that the schedule has set
    """


class _SerializerSubscriptionScheduleReleaseBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionScheduleReleaseBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    preserve_cancel_date: typing.Optional[bool] = pydantic.Field(
        alias="preserve_cancel_date", default=None
    )
