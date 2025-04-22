import pydantic
import typing
import typing_extensions


class ApplicationFeeRefundCreateBody(typing_extensions.TypedDict, total=False):
    """
    ApplicationFeeRefundCreateBody
    """

    amount: typing_extensions.NotRequired[int]

    directive: typing_extensions.NotRequired[str]

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerApplicationFeeRefundCreateBody(pydantic.BaseModel):
    """
    Serializer for ApplicationFeeRefundCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    directive: typing.Optional[str] = pydantic.Field(alias="directive", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
