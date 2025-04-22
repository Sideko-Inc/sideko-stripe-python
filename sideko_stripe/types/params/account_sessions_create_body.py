import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components import (
    AccountSessionsCreateBodyComponents,
    _SerializerAccountSessionsCreateBodyComponents,
)


class AccountSessionsCreateBody(typing_extensions.TypedDict, total=False):
    """
    AccountSessionsCreateBody
    """

    account: typing_extensions.Required[str]
    """
    The identifier of the account to create an Account Session for.
    """

    components: typing_extensions.Required[AccountSessionsCreateBodyComponents]
    """
    Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerAccountSessionsCreateBody(pydantic.BaseModel):
    """
    Serializer for AccountSessionsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    account: str = pydantic.Field(
        alias="account",
    )
    components: _SerializerAccountSessionsCreateBodyComponents = pydantic.Field(
        alias="components",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
