import pydantic
import typing
import typing_extensions


class AccountCapabilityCreateBody(typing_extensions.TypedDict, total=False):
    """
    AccountCapabilityCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    requested: typing_extensions.NotRequired[bool]
    """
    To request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the `requirements` arrays.
    
    If a capability isn't permanent, you can remove it from the account by passing false. Some capabilities are permanent after they've been requested. Attempting to remove a permanent capability returns an error.
    """


class _SerializerAccountCapabilityCreateBody(pydantic.BaseModel):
    """
    Serializer for AccountCapabilityCreateBody handling case conversions
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
    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
