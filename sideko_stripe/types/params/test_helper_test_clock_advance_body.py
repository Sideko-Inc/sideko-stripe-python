import pydantic
import typing
import typing_extensions


class TestHelperTestClockAdvanceBody(typing_extensions.TypedDict, total=False):
    """
    TestHelperTestClockAdvanceBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    frozen_time: typing_extensions.Required[int]
    """
    The time to advance the test clock. Must be after the test clock's current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future.
    """


class _SerializerTestHelperTestClockAdvanceBody(pydantic.BaseModel):
    """
    Serializer for TestHelperTestClockAdvanceBody handling case conversions
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
    frozen_time: int = pydantic.Field(
        alias="frozen_time",
    )
