import pydantic
import typing
import typing_extensions


class TestHelperTestClockCreateBody(typing_extensions.TypedDict, total=False):
    """
    TestHelperTestClockCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    frozen_time: typing_extensions.Required[int]
    """
    The initial frozen time for this test clock.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name for this test clock.
    """


class _SerializerTestHelperTestClockCreateBody(pydantic.BaseModel):
    """
    Serializer for TestHelperTestClockCreateBody handling case conversions
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
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
