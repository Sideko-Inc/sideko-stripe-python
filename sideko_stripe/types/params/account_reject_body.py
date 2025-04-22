import pydantic
import typing
import typing_extensions


class AccountRejectBody(typing_extensions.TypedDict, total=False):
    """
    AccountRejectBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    reason: typing_extensions.Required[str]
    """
    The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`.
    """


class _SerializerAccountRejectBody(pydantic.BaseModel):
    """
    Serializer for AccountRejectBody handling case conversions
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
    reason: str = pydantic.Field(
        alias="reason",
    )
