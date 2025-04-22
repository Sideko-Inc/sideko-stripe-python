import pydantic
import typing
import typing_extensions


class SetupIntentCancelBody(typing_extensions.TypedDict, total=False):
    """
    SetupIntentCancelBody
    """

    cancellation_reason: typing_extensions.NotRequired[
        typing_extensions.Literal["abandoned", "duplicate", "requested_by_customer"]
    ]
    """
    Reason for canceling this SetupIntent. Possible values are: `abandoned`, `requested_by_customer`, or `duplicate`
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerSetupIntentCancelBody(pydantic.BaseModel):
    """
    Serializer for SetupIntentCancelBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    cancellation_reason: typing.Optional[
        typing_extensions.Literal["abandoned", "duplicate", "requested_by_customer"]
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
